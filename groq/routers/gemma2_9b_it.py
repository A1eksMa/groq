from fastapi import APIRouter

router = APIRouter()

@router.post("/gemma2-9b-it")
async def gemma2_9b_it():
    return {"message": "This endpoint is under development."}
