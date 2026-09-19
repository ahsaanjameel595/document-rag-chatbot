from fastapi import APIRouter

from backend.memory.database import get_messages


router = APIRouter(
    prefix="/api/conversations",
    tags=["Conversations"],
)


@router.get("/{session_id}")
def get_conversation(session_id: str):

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