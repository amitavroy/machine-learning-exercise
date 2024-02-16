# https://www.youtube.com/watch?v=wrD-fZvT6UI&ab_channel=PromptEngineering
# https://colab.research.google.com/drive/1NaEyuFWCkDtkufHIsWQhfgPLHybXeYA1?usp=sharing#scrollTo=X2IMgDRGsVV4&uniqifier=1
# https://python.langchain.com/docs/use_cases/question_answering/quickstart

# pip install langchain
# pip install huggingface_hub
# pip install sentence_transformers

import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

# Document Loader
# loader = WebBaseLoader(
#     web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#     bs_kwargs=dict(
#         parse_only=bs4.SoupStrainer(
#             class_=("post-content", "post-title", "post-header")
#         )
#     ),
# )
loader = WebBaseLoader("https://www.amitavroy.com/articles/beyond-boundaries-how-frankenphp-redefines-php-application-runtimes-2024-01-01",
)
docs = loader.load()

import textwrap
def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Text Splitter
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(splits)

# Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain_community.vectorstores import FAISS

db = FAISS.from_documents(docs, embeddings)

query = "Can I create a binary using FrankenPHP?"
docs = db.similarity_search(query)

# print(wrap_text_preserve_newlines(str(docs[0].page_content)))

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "HUGGINGFACEHUB_API_TOKEN"
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import HuggingFaceHub

llm=HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":512})

from langchain import hub
prompt = hub.pull("rlm/rag-prompt")

example_messages = prompt.invoke(
    {"context": docs, "question": query}
).to_messages()
example_messages

print(example_messages[0].content)
