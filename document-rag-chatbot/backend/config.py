import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

PDF_PATH = os.getenv("PDF_PATH", "data/saas_faq.pdf")

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2",
)

TOP_K = int(os.getenv("TOP_K", "4"))

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))