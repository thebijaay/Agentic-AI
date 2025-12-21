from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from src.retrieval.vector_store import load_vector_store
from src.prompts.prompt_templates import get_system_prompt, get_user_prompt
from langchain_core.messages import AIMessage

class RAGAgent:
    def __init__(self, vector_store_path="faiss_index"):
        self.vector_store = load_vector_store(path=vector_store_path)
        self.llm = ChatOpenAI()
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self):
        system_prompt = get_system_prompt()
        user_prompt = get_user_prompt()

        prompt = ChatPromptTemplate.from_messages(
            [
                system_prompt,
                user_prompt,
            ]
        )

        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        retrieval_chain = create_retrieval_chain(
            self.vector_store.as_retriever(), question_answer_chain
        )

        return retrieval_chain

    def answer_query(self, query):
        response = self.qa_chain.invoke({"input": query})
        if isinstance(response.get("answer"), AIMessage):
            return response["answer"].content
        return response.get("answer", "")
