from langchain_groq import ChatGroq

from backend.config import GROQ_API_KEY


model = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=GROQ_API_KEY,
    temperature=0,
)


SYSTEM_PROMPT = """
You are a helpful document question-answering assistant.

Answer the user's question using ONLY the provided document context.

Rules:

1. Do not use outside knowledge.
2. If the answer is not available in the context, say:
   "I couldn't find this information in the document."
3. Do not invent facts.
4. Give a clear and concise answer.
5. Mention the relevant page number when available.

Document context:
"""


def generate_answer(question: str, documents):

    if not documents:

        return {
            "answer": "I couldn't find this information in the document.",
            "sources": [],
        }

    context_parts = []

    sources = []

    for document in documents:

        page = document.metadata.get("page")

        if page is not None:
            page = page + 1

        content = document.page_content

        context_parts.append(
            f"""
Page: {page}

Content:
{content}
"""
        )

        sources.append(
            {
                "page": page,
                "content": content,
            }
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""
{SYSTEM_PROMPT}

{context}

User question:
{question}

Answer:
"""

    response = model.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources,
    }