from langchain_community.document_loaders import WebBaseLoader
# loader = WebBaseLoader("https://docs.smith.langchain.com")
loader = WebBaseLoader("https://www.amitavroy.com/articles/beyond-boundaries-how-frankenphp-redefines-php-application-runtimes-2024-01-01")
docs = loader.load()

from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings()

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)


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


response = retrieval_chain.invoke({"input": "How can FrankenPHP speed things up?"})
print(response["answer"])
