from pathlib import Path

from fastapi import APIRouter

from backend.config import PDF_PATH


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"],
)


@router.get("/")
def document_info():

    path = Path(PDF_PATH)

    return {
        "name": path.name,
        "path": str(path),
        "type": "PDF",
    }