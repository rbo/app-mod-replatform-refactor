import os
from fastapi import FastAPI

port = int(os.environ.get("PORT", default=8080))
app = FastAPI()


@app.get("/service-b")
async def service_b():
    return {"message": "Hello from NEW service b"}


@app.get("/health")
async def health():
    return {"status": "UP"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, proxy_headers=True, server_header=False, access_log=False)