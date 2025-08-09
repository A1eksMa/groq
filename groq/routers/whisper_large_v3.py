from fastapi import APIRouter

router = APIRouter()

@router.post("/whisper-large-v3")
async def whisper_large_v3():
    return {"message": "This endpoint is under development."}
