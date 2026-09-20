from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.chat import router as chat_router
from backend.api.documents import router as documents_router
from backend.api.conversations import router as conversations_router


app = FastAPI(
    title="Document RAG Chatbot",
    description="PDF Question Answering RAG API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://document-rag-chatbot-seven.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)

app.include_router(documents_router)

app.include_router(conversations_router)


@app.get("/")
def root():

    return {
        "message": "Document RAG API is running."
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }