from fastapi import FastAPI
from rag import rag_answer

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Endee RAG API"}


@app.get("/ask")
def ask(q: str):

    ans = rag_answer(q)

    return {"answer": ans}