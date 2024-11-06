from fastapi import FastAPI
from app.routers import index, health, service_a, service_b

app = FastAPI()
app.include_router(index.router)
app.include_router(health.router)
app.include_router(service_a.router)
app.include_router(service_b.router)