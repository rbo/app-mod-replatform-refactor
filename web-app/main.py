import os
import logging
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

port = int(os.environ.get("PORT", default=3000))
backend_host = os.environ.get("BACKEND_HOST", default="localhost")
backend_port = int(os.environ.get("BACKEND_PORT", default=8080))

LOG = logging.getLogger("uvicorn.error")
app = FastAPI(openapi_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"active": "home"}
    )


@app.get("/service-a", response_class=HTMLResponse)
async def service_a(request: Request):
    json_response = await call_backend("service-a")

    return templates.TemplateResponse(
        request=request, name="service-a.html", context={"active": "service-a", "data": json_response}
    )


@app.get("/service-b", response_class=HTMLResponse)
async def service_b(request: Request):
    json_response = await call_backend("service-b")

    return templates.TemplateResponse(
        request=request, name="service-b.html", context={"active": "service-b", "data": json_response}
    )


@app.get("/health")
async def health():
    return {"status": "UP"}


async def call_backend(path: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f'http://{backend_host}:{backend_port}/{path}')
            response.raise_for_status()
            json_response = response.json()
            return json_response
    except Exception as e:
        LOG.error(f"Error response from {backend_host}:{backend_port}/{path}: {e}")
        return {"message": "Request error"}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, proxy_headers=True, server_header=False, access_log=False)
