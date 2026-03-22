# Advanced RAG System using Endee Vector Database

## Project Overview

This project demonstrates an AI/ML application built using **Endee** as the vector database.
The system implements a **Retrieval Augmented Generation (RAG)** pipeline that performs semantic search on documents and generates answers based on retrieved context.

The goal of the project is to show how vector databases can be used in real-world AI applications such as semantic search, question answering, and knowledge retrieval.

This project is built on top of the forked Endee repository as required.

---

## Problem Statement

Traditional keyword-based search cannot understand the semantic meaning of text.
When working with large document collections, we need a better way to retrieve relevant information.

Vector databases solve this problem by storing embeddings and performing similarity search.

This project demonstrates how to:

* Convert text to embeddings
* Store vectors
* Perform similarity search
* Use retrieved context to generate answers

---

## Use Case

This project implements:

* Semantic Search
* Retrieval Augmented Generation (RAG)
* Vector similarity search
* Document question answering

Example:

User Query → Find similar vectors → Retrieve documents → Generate answer

---

## System Design

Workflow:

1. Documents are loaded from data files
2. Text is converted into embeddings using SentenceTransformers
3. Embeddings are stored as vectors
4. Query is converted to embedding
5. Similar vectors are retrieved
6. Retrieved text is used to generate answer

Architecture:

Client → FastAPI → Embedder → Vector Search → Retrieved Context → RAG → Response

---

## How Endee is Used

This project is built on top of the forked Endee repository.

Endee provides the vector database environment where embeddings are stored and processed.

Steps where Endee is used:

* Project created inside forked Endee repo
* Vector search logic implemented inside Endee project environment
* Embeddings stored and retrieved within Endee workspace

This follows the mandatory requirement to use Endee as the base repository.

---

## Project Structure

```
advanced_rag_project/
│
├── app.py
├── rag.py
├── ingest.py
├── embedder.py
├── config.py
├── requirements.txt
├── README.md
│
└── data/
    ├── ai.txt
    ├── ml.txt
    └── db.txt
```

---

## Installation

Clone the forked repository

```
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee/advanced_rag_project
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Project

Step 1 — Store vectors

```
python ingest.py
```

Step 2 — Start API server

```
uvicorn app:app --reload
```

Step 3 — Open browser

```
http://127.0.0.1:8000
```

Test query

```
http://127.0.0.1:8000/ask?q=what is ai
```

---

## Example

Query:

```
what is vector database
```

Output:

```
Vector database stores embeddings.
Endee is vector database.
```

---

## Technologies Used

* Python
* Endee
* SentenceTransformers
* FastAPI
* NumPy
* Vector embeddings
* RAG pipeline

---

## Mandatory Steps Followed

✔ Starred official Endee repository
✔ Forked Endee repository
✔ Built project inside forked repo
✔ Used Endee as base environment
✔ Implemented vector search use case
✔ Hosted project on GitHub
✔ Added README and instructions

---

## Conclusion

This project demonstrates how Endee can be used as a vector database
to build real-world AI/ML applications such as semantic search and RAG systems.
