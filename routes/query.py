from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/")
async def query(question:str):
        # Implement your query logic here
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    # For demonstration, we will just return the question
    return {"question": question}