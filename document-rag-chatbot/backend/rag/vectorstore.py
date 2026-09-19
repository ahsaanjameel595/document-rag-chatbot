from pathlib import Path

from langchain_community.vectorstores import FAISS

from backend.config import PDF_PATH
from backend.rag.embeddings import get_embeddings
from backend.rag.loader import load_pdf
from backend.rag.splitter import split_documents


VECTORSTORE_DIR = Path("vectorstores")


def get_vectorstore():

    embeddings = get_embeddings()

    pdf_name = Path(PDF_PATH).stem

    index_path = VECTORSTORE_DIR / f"faiss_index_{pdf_name}"

    if index_path.exists():

        print("Loading existing FAISS index...")

        return FAISS.load_local(
            str(index_path),
            embeddings,
            allow_dangerous_deserialization=True,
        )

    print("Creating FAISS index...")

    documents = load_pdf(PDF_PATH)

    chunks = split_documents(documents)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings,
    )

    VECTORSTORE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    vectorstore.save_local(
        str(index_path)
    )

    print(f"FAISS index saved to {index_path}")

    return vectorstore