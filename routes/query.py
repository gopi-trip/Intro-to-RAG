from fastapi import APIRouter, HTTPException
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

router = APIRouter(prefix="/query", tags=["Query"])

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="sample_collection",
    url="http://localhost:6333"
)


@router.post("/")
async def query(question:str):
        # Implement your query logic here
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    # For demonstration, we will just return the question
    search_results = vector_db.similarity_search(query=question)
    print(search_results)
    return {
        "Response": search_results
    }