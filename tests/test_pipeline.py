import unittest
from unittest.mock import patch
import os
from dotenv import load_dotenv
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.messages import AIMessage
from src.agent.rag_agent import RAGAgent
from src.ingestion.document_loader import load_documents
from src.ingestion.text_processing import chunk_documents
from src.retrieval.vector_store import create_vector_store, save_vector_store

class TestRAGPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.vector_store_path = "test_faiss_index"

        # Create dummy data for testing
        if not os.path.exists("test_data"):
            os.makedirs("test_data")
        with open("test_data/test.txt", "w") as f:
            f.write("This is a test document. The capital of France is Paris.")

        # Ingest and process documents
        documents = load_documents("test_data")
        chunks = chunk_documents(documents)

        # Create and save the vector store
        vector_store = create_vector_store(chunks)
        save_vector_store(vector_store, cls.vector_store_path)

    @patch('langchain_openai.ChatOpenAI._generate')
    def test_end_to_end_pipeline(self, mock_generate):
        # Configure the mock to return a ChatResult
        mock_generate.return_value = ChatResult(generations=[ChatGeneration(message=AIMessage(content="Paris is the capital of France."))])

        # Initialize the RAG agent
        agent = RAGAgent(vector_store_path=self.vector_store_path)

        # Ask a question
        query = "What is the capital of France?"
        response = agent.answer_query(query)

        # Check if the response contains the expected answer
        self.assertIn("Paris", response)

    @classmethod
    def tearDownClass(cls):
        # Clean up the test data and vector store
        import shutil
        if os.path.exists("test_data"):
            shutil.rmtree("test_data")
        if os.path.exists(cls.vector_store_path):
            shutil.rmtree(cls.vector_store_path)

if __name__ == '__main__':
    unittest.main()
