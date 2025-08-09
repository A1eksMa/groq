from fastapi import APIRouter

router = APIRouter()

@router.post("/compound-beta")
async def compound_beta():
    return {"message": "This endpoint is under development."}
