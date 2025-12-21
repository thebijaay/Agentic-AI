from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(chunks, embedding_model_name='sentence-transformers/all-MiniLM-L6-v2'):
    """
    Creates a FAISS vector store from document chunks and saves it to disk.
    """
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

def save_vector_store(vector_store, path="faiss_index"):
    """
    Saves the vector store to the specified path.
    """
    vector_store.save_local(path)

def load_vector_store(path="faiss_index", embedding_model_name='sentence-transformers/all-MiniLM-L6-v2'):
    """
    Loads the vector store from the specified path.
    """
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    # SECURITY WARNING: Loading FAISS indexes with allow_dangerous_deserialization=True
    # can be dangerous if the source of the file is untrusted, as it can lead to
    # arbitrary code execution. Only load files from sources you trust.
    vector_store = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    return vector_store
