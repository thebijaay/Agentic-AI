# RAG Agent: A Retrieval-Augmented Generation System

## Introduction

This project provides a comprehensive implementation of a Retrieval-Augmented Generation (RAG) agent. The system is designed to answer user queries by leveraging a knowledge base of documents. It ingests documents in various formats (PDF, TXT, MD), processes them into a searchable vector store, and uses a language model to generate contextually relevant answers. This publication details the architecture, methodology, and usage of the agent, serving as a guide for understanding and deploying RAG-based solutions.

## System Architecture

The RAG agent is built on a modular architecture that separates concerns for document handling, retrieval, and generation. The core components are:

-   **Document Ingestion Pipeline**: Loads documents, splits them into manageable chunks, and generates embeddings.
-   **Vector Store**: A FAISS-powered database that stores the document embeddings for efficient similarity searches.
-   **RAG Agent**: The central component that orchestrates the retrieval and generation process. It takes a user query, retrieves relevant context from the vector store, and passes it to the language model.
-   **Language Model (LLM)**: The core intelligence of the agent, responsible for generating human-like answers based on the provided context.

### System Architecture Diagram
```
+------------------------+
|   User Interface       |
| (Command Line)         |
+-----------+------------+
            |
            v
+-----------+------------+
|       main.py          |
| (Application Logic)    |
+-----------+------------+
            |
            v
+-----------+------------+      +------------------------+
|     RAGAgent           |----->|   Vector Store         |
| (src/agent/rag_agent.py)|      | (FAISS)                |
+-----------+------------+      +-----------+------------+
            |                           ^
            v                           |
+-----------+------------+      +-------+----------------+
| Language Model (LLM)   |      | Document Ingestion     |
| (OpenAI API)           |      | (src/ingestion/*)      |
+------------------------+      +------------------------+
```

## Methodology

### Document Ingestion Flow

The document ingestion process is the first step in building the agent's knowledge base. It consists of the following steps:
1.  **Loading**: Documents from the `data/` directory are loaded using `langchain`'s document loaders, which support PDF, TXT, and Markdown formats.
2.  **Chunking**: The loaded documents are split into smaller, overlapping chunks using a `RecursiveCharacterTextSplitter`. This ensures that semantic context is preserved while preparing the text for embedding.
3.  **Embedding**: Each chunk is converted into a numerical vector using a sentence-transformer model (`all-MiniLM-L6-v2`). These embeddings capture the semantic meaning of the text.
4.  **Storage**: The embeddings and their corresponding text chunks are stored in a FAISS vector store, which is then saved to disk for later use.

### RAG/Agent Workflow Diagram
```
+--------------+       +-------------------+       +-----------------+
|  User Query  |------>|  Query Embedding  |------>| Similarity      |
|              |       |                   |       | Search (FAISS)  |
+--------------+       +-------------------+       +--------+--------+
                                                             |
                                                             v
+--------------+       +-------------------+       +--------+--------+
| Final Answer |<------| Answer Generation |<------| Contextual      |
|              |       | (LLM)             |       | Prompting       |
+--------------+       +-------------------+       +-----------------+
```

### Query Processing and Optimization

When a user submits a query, the following steps are executed:
1.  **Query Embedding**: The user's query is converted into an embedding using the same sentence-transformer model that was used for the documents.
2.  **Similarity Search**: The query embedding is used to perform a similarity search in the FAISS vector store. The retriever fetches the most relevant document chunks based on cosine similarity.
3.  **Contextual Prompting**: The retrieved document chunks are formatted into a context block and inserted into a prompt template, along with the original user query.
4.  **Answer Generation**: The final prompt is sent to the language model (e.g., GPT-3.5), which generates a concise and relevant answer based on the provided context.

The primary optimization in this system is the use of a vector store, which allows for highly efficient retrieval of relevant documents, even from a large corpus.

### How Agentic Reasoning and RAG Work Together

This project implements a foundational RAG pattern. While it doesn't have a complex agentic loop with multiple tools, it demonstrates the core principle of an agent: **acting to retrieve information to better inform its response**. The agent's "tool" is the vector store retriever.

A more advanced agentic system could be built on top of this by:
-   **Adding more tools**: For example, a web search tool to find real-time information if the answer is not in the local documents.
-   **Implementing a ReAct Loop**: The agent could reason about the user's query, decide if it needs to use the retriever, and then act. If the initial retrieval is insufficient, it could reason again and perform another search or use a different tool.
-   **Conversational Memory**: The agent could be given memory to remember past interactions, allowing it to answer follow-up questions more effectively.

## Installation & Usage

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up environment variables:**
    -   Create a `.env` file in the root directory.
    -   Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY=your_api_key_here
        ```
4.  **Add your documents:**
    -   Place your documents (PDF, TXT, or Markdown) in the `data` directory.

### Running the Agent

To run the RAG agent, execute the following command:
```bash
python main.py
```
The application will first create the vector store if it doesn't exist, and then it will enter an interactive loop where you can ask questions.

### Example Usage

```
RAG Agent is ready. Ask your questions (type 'exit' to quit).
> What is the capital of France?
Paris is the capital of France.
```

## Project Structure

```
├── data/
├── docs/
│   └── architecture.txt
├── images/
├── src/
│   ├── agent/
│   │   └── rag_agent.py
│   ├── ingestion/
│   │   ├── document_loader.py
│   │   └── text_processing.py
│   ├── prompts/
│   │   └── prompt_templates.py
│   ├── retrieval/
│   │   └── vector_store.py
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```
