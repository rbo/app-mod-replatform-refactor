import os
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

backend_host = os.environ.get("BACKEND_HOST", default="localhost")
backend_port = int(os.environ.get("BACKEND_PORT", default=8080))

app = FastAPI(openapi_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"active": "home"}
    )


@app.get("/service-a", response_class=HTMLResponse)
def service_a(request: Request):
    json_response = call_backend("service-a")

    return templates.TemplateResponse(
        request=request, name="service-a.html", context={"active": "service-a", "data": json_response}
    )


@app.get("/service-b", response_class=HTMLResponse)
def service_b(request: Request):
    json_response = call_backend("service-b")

    return templates.TemplateResponse(
        request=request, name="service-b.html", context={"active": "service-b", "data": json_response}
    )


@app.get("/health")
def health():
    return {"status": "UP"}


def call_backend(path: str):
    try:
        response = requests.get(f'http://{backend_host}:{backend_port}/{path}')
        return response.json()
    except Exception as e:
        print("An error occurred:", e)
        return {"message": "Request error"}
