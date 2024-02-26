from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

DB_FAISS_PATH="data/db_faiss"

# Download Sentence Transformers Embedding From Hugging Face
# Loading it here so that I can use it in both cases i.e.
# when the vector store is present and not present
embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

# Generating the FAISS DB here so that the main code is simpler.
loader = CSVLoader(file_path="data/faq.csv", encoding="utf-8", csv_args={'delimiter': ','})
data = loader.load()

# Split the text into Chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
text_chunks = text_splitter.split_documents(data)

# Converting the text Chunks into embeddings and saving the embeddings into FAISS Knowledge Base
docsearch = FAISS.from_documents(text_chunks, embeddings)
docsearch.save_local(DB_FAISS_PATH)
