from fastapi import APIRouter

router = APIRouter()

@router.post("/allam-2-7b")
async def allam_2_7b():
    return {"message": "This endpoint is under development."}
