from fastapi import APIRouter

router = APIRouter()


@router.get("/service-a")
async def index():
    return {"message": "Hello from Service a"}
