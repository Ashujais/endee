import numpy as np
import endee

from embedder import get_embedding


vectors = np.load("vectors.npy", allow_pickle=True)
texts = np.load("texts.npy", allow_pickle=True)


def search_docs(query):

    q = get_embedding([query])[0]

    sims = vectors @ q

    idx = sims.argsort()[-3:][::-1]

    return [texts[i] for i in idx]


def rag_answer(query):

    docs = search_docs(query)

    context = " ".join(docs)

    answer = f"""
Context:
{context}

Question:
{query}

Answer:
{context}
"""

    return answer