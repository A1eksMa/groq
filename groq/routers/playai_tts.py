from fastapi import APIRouter

router = APIRouter()

@router.post("/playai-tts")
async def playai_tts():
    return {"message": "This endpoint is under development."}
