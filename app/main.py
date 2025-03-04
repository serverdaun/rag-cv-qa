import uvicorn
from fastapi import FastAPI
from query import rag_query

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello, this is QA bot for my CV. Feel free to ask any questions!"
    }

@app.post("/query")
def query(question: str):
    return rag_query(question)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
