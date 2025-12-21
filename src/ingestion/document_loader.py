import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_documents(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
            documents.extend(loader.load())
        elif filename.endswith(".txt"):
            loader = TextLoader(filepath)
            documents.extend(loader.load())
        elif filename.endswith(".md"):
            loader = TextLoader(filepath, encoding="utf-8")
            documents.extend(loader.load())
    return documents
