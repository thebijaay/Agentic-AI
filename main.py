import os
from dotenv import load_dotenv
from src.agent.rag_agent import RAGAgent
from src.ingestion.document_loader import load_documents
from src.ingestion.text_processing import chunk_documents
from src.retrieval.vector_store import create_vector_store, save_vector_store

def main():
    load_dotenv()

    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found. Please set it in a .env file.")
        return

    vector_store_path = "faiss_index"

    # Check if the vector store exists
    if not os.path.exists(vector_store_path):
        print("Vector store not found. Creating a new one...")

        # Create a data directory if it doesn't exist
        if not os.path.exists("data"):
            os.makedirs("data")

        # If the data directory is empty, create a dummy file for ingestion
        if not os.listdir("data"):
            with open("data/sample.txt", "w") as f:
                f.write("This is a sample document for the RAG agent.")

        # Ingest and process documents
        documents = load_documents("data")
        chunks = chunk_documents(documents)

        # Create and save the vector store
        vector_store = create_vector_store(chunks)
        save_vector_store(vector_store, vector_store_path)
        print("Vector store created and saved.")

    # Initialize the RAG agent
    agent = RAGAgent(vector_store_path=vector_store_path)

    print("RAG Agent is ready. Ask your questions (type 'exit' to quit).")
    while True:
        query = input("> ")
        if query.lower() == "exit":
            break
        response = agent.answer_query(query)
        print(response)

if __name__ == "__main__":
    main()
