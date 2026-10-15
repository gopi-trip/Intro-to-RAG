from fastapi import FastAPI
from routes.query import router

app = FastAPI(
    title="RAG API",
    description="This is a RAG API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "Message":"Welcome to the RAG API"
    }

app.include_router(router)