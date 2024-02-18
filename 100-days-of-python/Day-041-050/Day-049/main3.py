import sys
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
# loader = WebBaseLoader("https://docs.smith.langchain.com")
# loader = WebBaseLoader("https://www.aljazeera.com/news/2024/2/16/check-on-quid-pro-quo-will-indias-electoral-bonds-ban-hurt-modi")
# docs = loader.load()
loader = PyPDFLoader("/Users/amitavroy/code/personal/machine_learning/100-days-of-python/Day-49/sc_verdict.pdf")
pages = loader.load_and_split()

from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings()

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter()
# documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(pages, embeddings)


# Running the LLM part for output
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer."),
#     ("user", "{input}")
# ])

# from langchain_core.output_parsers import StrOutputParser
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
# output = chain.invoke({"input": "how can langsmith help with testing?"})
# print(output)


from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

from langchain.chains import create_retrieval_chain
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)


response = retrieval_chain.invoke({"input": "What is this verdict all about?"})
print(response["answer"])
