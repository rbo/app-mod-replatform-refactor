from fastapi import APIRouter

router = APIRouter()


@router.get("/service-b")
async def index():
    return {"message": "Hello from Service b"}