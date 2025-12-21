# RAG Agent Project

This project implements a Retrieval-Augmented Generation (RAG) agent that can answer questions based on a provided set of documents.

## Architecture Overview

The RAG agent is built using the following components:

-   **Document Loaders**: Load documents from various sources (PDF, TXT, Markdown).
-   **Text Splitters**: Chunk the loaded documents into smaller, manageable pieces.
-   **Embedding Models**: Convert the document chunks into numerical vectors.
-   **Vector Store**: Store the document vectors and allow for efficient retrieval.
-   **Retriever**: Retrieve relevant document chunks based on a user query.
-   **Prompt Templates**: Define the prompts used to generate answers.
-   **LLM**: The language model used to generate answers.
-   **QA Chain**: The main chain that ties all the components together.

### Architecture Diagram

```
+-----------------+      +----------------------+      +-----------------+
|   Documents     |----->| Document Ingestion   |----->|   Vector Store  |
| (PDF, TXT, MD)  |      | (Loader, Chunker)    |      |     (FAISS)     |
+-----------------+      +----------------------+      +-----------------+
        ^                                                    |
        |                                                    |
+-----------------+      +----------------------+      +-----------------+
|   User Query    |----->|      RAG Agent       |<-----|    Retriever    |
+-----------------+      | (LLM, Prompting)     |      +-----------------+
        |                +----------------------+
        |                           |
        v                           v
+-----------------+      +----------------------+
|     Answer      |<-----|  Answer Generation   |
+-----------------+      +----------------------+
```

## How RAG Works in This Project

1.  **Document Ingestion**: Documents are loaded from the `data` directory, processed, and stored in a FAISS vector store.
2.  **Query Processing**: When a user asks a question, the RAG agent retrieves the most relevant document chunks from the vector store.
3.  **Answer Generation**: The retrieved document chunks are then used as context for the language model, which generates an answer to the user's question.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```
2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your environment variables:**
    -   Create a `.env` file in the root directory of the project.
    -   Add the following line to the `.env` file:
        ```
        OPENAI_API_KEY=your_api_key_here
        ```
4.  **Add your documents:**
    -   Place your documents (PDF, TXT, or Markdown) in the `data` directory.
5.  **Run the RAG agent:**
    ```bash
    python main.py
    ```

## Example Usage

Once the RAG agent is running, you can ask questions in the command line:

```
> What is the capital of France?
Paris
```

## Environment Variables

-   `OPENAI_API_KEY`: Your OpenAI API key.

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
