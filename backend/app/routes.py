from fastapi import APIRouter, HTTPException, Query
from app.utils import setup_chain

router = APIRouter()

# Initialize the chain
chain = setup_chain()

@router.post("/ask")
async def ask_question(question: str = Query(..., description="The question to ask the chatbot")):
    try:
        print(f"Received question: {question}")
        response = chain.run({"question": question})
        print(f"Generated response: {response}")
        return {"response": response}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
