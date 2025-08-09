from fastapi import APIRouter

router = APIRouter()

@router.post("/compound-beta-mini")
async def compound_beta_mini():
    return {"message": "This endpoint is under development."}
