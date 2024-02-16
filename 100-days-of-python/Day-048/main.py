{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import getpass\n",
    "import os\n",
    "\n",
    "os.environ[\"OPENAI_API_KEY\"] = getpass.getpass()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import bs4\n",
    "from langchain import hub\n",
    "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
    "from langchain_community.document_loaders import WebBaseLoader\n",
    "from langchain_community.vectorstores import Chroma\n",
    "from langchain_core.output_parsers import StrOutputParser\n",
    "from langchain_core.runnables import RunnablePassthrough\n",
    "from langchain.embeddings import HuggingFaceEmbeddings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load, chunk and index the contents of the blog.\n",
    "loader = WebBaseLoader(\n",
    "    web_paths=(\"https://lilianweng.github.io/posts/2023-06-23-agent/\",),\n",
    "    bs_kwargs=dict(\n",
    "        parse_only=bs4.SoupStrainer(\n",
    "            class_=(\"post-content\", \"post-title\", \"post-header\")\n",
    "        )\n",
    "    ),\n",
    ")\n",
    "docs = loader.load()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)\n",
    "splits = text_splitter.split_documents(docs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "66"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(splits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "Could not import sentence_transformers python package. Please install it with `pip install sentence-transformers`.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/langchain_community/embeddings/huggingface.py:59\u001b[0m, in \u001b[0;36mHuggingFaceEmbeddings.__init__\u001b[0;34m(self, **kwargs)\u001b[0m\n\u001b[1;32m     58\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m---> 59\u001b[0m     \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msentence_transformers\u001b[39;00m\n\u001b[1;32m     61\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mImportError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m exc:\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'sentence_transformers'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[16], line 4\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# Embeddings\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01membeddings\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m HuggingFaceEmbeddings\n\u001b[0;32m----> 4\u001b[0m embeddings \u001b[38;5;241m=\u001b[39m HuggingFaceEmbeddings()\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/langchain_community/embeddings/huggingface.py:62\u001b[0m, in \u001b[0;36mHuggingFaceEmbeddings.__init__\u001b[0;34m(self, **kwargs)\u001b[0m\n\u001b[1;32m     59\u001b[0m     \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msentence_transformers\u001b[39;00m\n\u001b[1;32m     61\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mImportError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m exc:\n\u001b[0;32m---> 62\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mImportError\u001b[39;00m(\n\u001b[1;32m     63\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCould not import sentence_transformers python package. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     64\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPlease install it with `pip install sentence-transformers`.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     65\u001b[0m     ) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mexc\u001b[39;00m\n\u001b[1;32m     67\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclient \u001b[38;5;241m=\u001b[39m sentence_transformers\u001b[38;5;241m.\u001b[39mSentenceTransformer(\n\u001b[1;32m     68\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmodel_name, cache_folder\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcache_folder, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmodel_kwargs\n\u001b[1;32m     69\u001b[0m )\n",
      "\u001b[0;31mImportError\u001b[0m: Could not import sentence_transformers python package. Please install it with `pip install sentence-transformers`."
     ]
    }
   ],
   "source": [
    "# Embeddings\n",
    "from langchain.embeddings import HuggingFaceEmbeddings\n",
    "\n",
    "embeddings = HuggingFaceEmbeddings()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
