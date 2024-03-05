import requests
from bs4 import BeautifulSoup
from transformers import BertTokenizer, BertModel
import faiss
import numpy as np

def get_article_data(url: str):
    if not url:
        raise ValueError("Invalid URL provided.")
    
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find("title")
        article_title = title_tag.text.strip() if title_tag else "Untitled"

        article_content_tag = soup.find("main", class_="article-full")
        if article_content_tag:
            article_content = article_content_tag.text.strip()  # Extract and clean the text content
            return article_title, article_content
        else:
            print(f"Content not found in <div> tag with class 'article-full' on {url}.")
            return None, None

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error crawling {url}: {e}")
        return None, None

def chunk_text(text, chunk_size=1000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def encode_text(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model(**inputs)
    encoded_vector = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
    return encoded_vector

def save_faiss_index(index, filename="faiss_index.index"):
    faiss.write_index(index, filename)

def load_faiss_index(filename="faiss_index.index"):
    try:
        return faiss.read_index(filename)
    except:
        return None

def main():
    # Specify the URLs of the articles
    urls = [
        'https://www.amitavroy.com/articles/beyond-boundaries-how-frankenphp-redefines-php-application-runtimes-2024-01-01',
        'https://www.amitavroy.com/articles/the-future-is-low-code-adapting-to-the-inevitable-2023-10-24',
        'https://www.amitavroy.com/articles/what-is-next-js-incremental-static-generation-isr-a-complete-guide-2023-10-02',
        'https://www.amitavroy.com/articles/how-saloon-php-helped-me-changing-my-newsletter-integration-in-minutes-2023-09-24',
        'https://www.amitavroy.com/articles/multi-tenant-apps-and-why-they-are-efficient-2023-09-16',
        'https://www.amitavroy.com/articles/why-use-saloon-connect-third-party-api'
    ]

    # Initialize BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")

    # Load or create FAISS index
    index = load_faiss_index()
    if index is None:
        index = faiss.IndexFlatIP(768)  # Assuming 768 is the size of BERT encoding

    # Initialize text_chunks list outside the loop
    titles = []
    text_chunks = []

    for url in urls:
        # Get the content of the article
        article_title, article_content = get_article_data(url)

        if article_title is not None and article_content is not None:
            titles.append(article_title)

            # Chunk the text
            chunks = chunk_text(article_content)
            text_chunks.extend(chunks)  # Extend the list with chunks for each article

            encoded_vectors = []
            for chunk in chunks:
                encoded_vector = encode_text(chunk, tokenizer, model)
                index.add(np.array([encoded_vector]))
                encoded_vectors.append(encoded_vector)

    # Save the FAISS index to a file
    save_faiss_index(index)

    # Search for similar content (example with a single query)
    search_query = "laravel saloon"
    query_vector = encode_text(search_query, tokenizer, model)

    D, I = index.search(np.array([query_vector]), k=5)  # Adjust k based on the number of similar documents you want

    print("Similar documents:")
    for i, idx in enumerate(I[0]):
        if 0 <= idx < len(titles):
            similarity_score = D[0][i]
            similar_title = titles[idx]
            print(f"Similarity Score: {similarity_score}, Title: {similar_title}")

if __name__ == "__main__":
    main()
