import bs4
from langchain_community.document_loaders import WebBaseLoader

# Document Loader
loader = WebBaseLoader("https://www.amitavroy.com/articles/beyond-boundaries-how-frankenphp-redefines-php-application-runtimes-2024-01-01",
)
docs = loader.load()
print(docs)
