from fastapi import APIRouter

router = APIRouter()


@router.get("/health/readiness")
async def readiness():
    return {"message": "Ready"}


@router.get("/health/liveness")
async def liveness():
    return {"message": "Ready"}
