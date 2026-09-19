# Document RAG Chatbot

A full-stack document Q&A chatbot built with a Python FastAPI backend and a React/Vite frontend.

## Project structure

- `backend/` contains the API, retrieval logic, and database access.
- `frontend/` contains the React app UI.
- `data/` stores local PDF documents.
- `vectorstores/` stores embedding indexes.
- `evaluation/` holds evaluation scripts and reference datasets.

## Quick start

1. Create a virtual environment and install dependencies.
2. Start the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```
3. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Environment

Copy the values in `.env` and add your API keys before running the app.
