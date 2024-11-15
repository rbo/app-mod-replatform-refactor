import os
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

port = int(os.environ.get("PORT", default=3000))
backend_host = os.environ.get("BACKEND_HOST", default="localhost")
backend_port = int(os.environ.get("BACKEND_PORT", default=8080))
backend_timeout = int(os.environ.get("BACKEND_TIMEOUT", default=3))

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"active": "home"}
    )


@app.get("/service-a", response_class=HTMLResponse)
async def service_a(request: Request):
    try:
        response = requests.get(f'http://{backend_host}:{backend_port}/service-a', timeout=backend_timeout)
        json_response = response.json()
    except Exception as e:
        print("An error occurred:", e)
        json_response = {"message": "Request error"}

    return templates.TemplateResponse(
        request=request, name="service-a.html", context={"active": "service-a", "data": json_response}
    )


@app.get("/service-b", response_class=HTMLResponse)
async def service_b(request: Request):
    try:
        response = requests.get(f'http://{backend_host}:{backend_port}/service-a', timeout=backend_timeout)
        json_response = response.json()
    except Exception as e:
        print("An error occurred:", e)
        json_response = {"message": "Request error"}

    return templates.TemplateResponse(
        request=request, name="service-b.html", context={"active": "service-b", "data": json_response}
    )


@app.get("/health")
async def health():
    return {"status": "UP"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, proxy_headers=True, server_header=False, access_log=False)