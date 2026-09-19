import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from backend.memory.database import (
    get_messages,
    save_message,
)

from backend.rag.retriever import retrieve_documents
from backend.rag.generator import generate_answer


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):

    question: str

    session_id: str | None = None


@router.post("/")
def chat(request: ChatRequest):

    session_id = request.session_id or str(uuid.uuid4())

    question = request.question.strip()

    if not question:

        return {
            "error": "Question cannot be empty."
        }

    save_message(
        session_id,
        "user",
        question,
    )

    documents = retrieve_documents(question)

    result = generate_answer(
        question,
        documents,
    )

    save_message(
        session_id,
        "assistant",
        result["answer"],
    )

    return {
        "session_id": session_id,
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"],
    }


@router.get("/{session_id}")
def history(session_id: str):

    messages = get_messages(session_id)

    return {
        "session_id": session_id,
        "messages": [
            {
                "role": role,
                "content": content,
            }
            for role, content in messages
        ],
    }