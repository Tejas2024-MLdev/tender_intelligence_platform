# Tender Intelligence Platform

AI-powered Tender Analysis & Document Intelligence Platform.

## Features

- JWT Authentication
- Multi-Tenant Architecture
- PostgreSQL Metadata Store
- MinIO Object Storage
- Document Upload APIs
- Async FastAPI Backend

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- MinIO
- Docker

## Project Structure

backend/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── services/

## Setup

1. Clone repository
2. Create .env from .env.example
3. Start PostgreSQL and MinIO
4. Run migrations

```bash
alembic upgrade head
```

5. Start application

```bash
python -m uvicorn backend.main:app --reload
```