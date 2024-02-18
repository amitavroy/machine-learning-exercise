from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import sys
import os

DB_FAISS_PATH="data/db_faiss"

# Download Sentence Transformers Embedding From Hugging Face
# Loading it here so that I can use it in both cases i.e.
# when the vector store is present and not present
embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
if os.path.exists(DB_FAISS_PATH):
    print('Loading existing FAISS vector store...')
    docsearch = FAISS.load_local(DB_FAISS_PATH, embeddings=embeddings)
else: 
    # Loading the CSV data here
    loader = CSVLoader(file_path="data/2019.csv", encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()

    # Split the text into Chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data)

    # Converting the text Chunks into embeddings and saving the embeddings into FAISS Knowledge Base
    docsearch = FAISS.from_documents(text_chunks, embeddings)
    docsearch.save_local(DB_FAISS_PATH)

# query = "What is the value of GDP per capita of Finland provided in the data?"
# docs = docsearch.similarity_search(query, k=3)

# print("Result", docs)

llm = CTransformers(
    model="models/llama-2-7b-chat.ggmlv3.q3_K_S.bin", 
    model_type="llama",
    max_new_tokens=512,
    temperature=0.1)

qa = ConversationalRetrievalChain.from_llm(llm, retriever=docsearch.as_retriever())

while True:
    chat_history = []
    #query = "What is the value of  GDP per capita of Finland provided in the data?"
    query = input(f"Input Prompt: ")
    if query == 'exit':
        print('Exiting')
        sys.exit()
    if query == '':
        continue
    result = qa({"question":query, "chat_history":chat_history})
    print("Response: ", result['answer'])
