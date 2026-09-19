from backend.config import TOP_K
from backend.rag.vectorstore import get_vectorstore


vectorstore = get_vectorstore()

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": TOP_K
    },
)


def retrieve_documents(query: str):

    documents = retriever.invoke(query)

    return documents