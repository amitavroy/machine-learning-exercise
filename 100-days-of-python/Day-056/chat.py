from langchain_community.llms import CTransformers
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import time

DB_FAISS_PATH="data/db_faiss"
embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

llm = CTransformers(
    model="../common/llama-2-7b-chat.ggmlv3.q8_0.bin", 
    model_type="llama",
    max_new_tokens=512,
    temperature=0.1)

docsearch = FAISS.load_local(DB_FAISS_PATH, embeddings=embeddings)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=docsearch.as_retriever())

chat_history = []
while True:
    #query = "What is the value of  GDP per capita of Finland provided in the data?"
    query = input(f"Input Prompt: ")
    if query == 'exit':
        print('Exiting')
        sys.exit()
    if query == '':
        continue

    start_time = time.time()
    result = qa({"question":query, "chat_history":chat_history})
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Response: ", result['answer'], "\nTime take:", elapsed_time)
