# Advanced RAG System using Endee Vector Database

## Project Overview

This project demonstrates a Retrieval Augmented Generation (RAG) system
using Endee as the vector database.

The system performs semantic search on documents and generates answers
based on retrieved context.

## Problem Statement

Traditional keyword search cannot understand semantic meaning.
We need vector search to retrieve relevant information.

## Solution

We use:

User Query
→ Embedding
→ Endee Vector Search
→ Top Documents
→ RAG
→ Answer

## System Design

Client → FastAPI → Embedder → Endee → Retrieved Docs → RAG → Response

## Tech Stack

- Python
- Endee Vector DB
- SentenceTransformers
- FastAPI
- RAG pipeline

## How Endee is used

Endee stores vector embeddings and performs similarity search.
Documents are converted to embeddings and stored in collection.
Queries are embedded and searched using vector similarity.

## Setup

git clone https://github.com/USERNAME/endee.git

cd endee/advanced_rag_project

pip install -r requirements.txt

## Run

python ingest.py

uvicorn app:app --reload

Open:

http://127.0.0.1:8000/ask?q=what is ai

## Features

✔ Semantic Search  
✔ RAG  
✔ Vector DB  
✔ Multi file ingestion  
✔ API  
✔ Endee integration  