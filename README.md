# Tender Intelligence Platform

AI-powered Tender Analysis and Retrieval-Augmented Generation (RAG) platform that enables users to upload tender documents, perform semantic search, and interact with documents using natural language.

## Features

### Authentication & Security

* JWT-based authentication
* Multi-tenant architecture
* Organization-level data isolation

### Document Management

* PDF document upload
* MinIO object storage
* Document metadata management

### AI & RAG Pipeline

* PDF text extraction using PyMuPDF
* Intelligent document chunking
* Embedding generation using Sentence Transformers
* Vector storage using Qdrant
* Semantic search
* Context-aware question answering using LLMs

### AI Chat

* Document-aware conversational interface
* Context retrieval from vector database
* LLM-powered answer generation
* Source attribution support

## System Architecture

User Uploads PDF
↓
MinIO Storage
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Qdrant Vector Database
↓
Semantic Retrieval
↓
LLM (OpenRouter / Ollama)
↓
Answer Generation

## Tech Stack

### Backend

* FastAPI
* Python 3.14
* SQLAlchemy Async
* Alembic

### Database

* PostgreSQL

### Object Storage

* MinIO

### Vector Database

* Qdrant

### AI/ML

* Sentence Transformers
* OpenRouter
* Ollama (planned)

### DevOps

* Docker
* GitHub

## API Endpoints

### Authentication

POST /auth/register

POST /auth/login

GET /auth/me

### Documents

POST /documents/upload

GET /documents

POST /documents/{document_id}/ingest

### Search

POST /search

### Chat

POST /chat

## Example Workflow

1. Upload a PDF tender document
2. Ingest the document into the RAG pipeline
3. Generate embeddings and store vectors in Qdrant
4. Ask questions about the tender
5. Receive context-aware answers

## Future Roadmap

* OCR support for scanned PDFs
* Hybrid Retrieval (BM25 + Vector Search)
* Tender Summary API
* Eligibility Criteria Extraction
* EMD Details Extraction
* Important Dates Extraction
* Tender Compliance Analysis
* Chat History & Memory
* Ollama Integration
* Kubernetes Deployment

## Project Status

Current Version: MVP

Completed:

* Authentication
* Document Upload
* MinIO Integration
* RAG Pipeline
* Semantic Search
* LLM Integration
* Multi-Tenant Architecture

In Progress:

* Source Attribution
* Tender Intelligence APIs

Planned:

* OCR
* Hybrid Retrieval
* Agentic Workflows

## GitHub Repository

https://github.com/Tejas2024-MLdev/tender_intelligence_platform
