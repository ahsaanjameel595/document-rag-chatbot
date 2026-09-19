from backend.config import TOP_K
from backend.rag.vectorstore import get_vectorstore


retriever = None


def get_retriever():
    global retriever

    if retriever is None:
        vectorstore = get_vectorstore()

        retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": TOP_K
            },
        )

    return retriever


def retrieve_documents(query: str):

    retriever = get_retriever()

    documents = retriever.invoke(query)

    return documents