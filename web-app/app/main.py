import os
from flask import Flask, render_template
import requests

port = int(os.environ.get("PORT", default=3000))
backend_host = os.environ.get("BACKEND_HOST", default="localhost")
backend_port = int(os.environ.get("BACKEND_PORT", default=8080))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", active="home")


@app.route('/service-a')
def service_a():
    try:
        response = requests.get(f'http://{backend_host}:{backend_port}/service-a')
        json_response = response.json()
    except Exception as e:
        print("An error occurred:", e)
        json_response = {"message": "Request error"}

    return render_template("service-a.html", active="service-a", data=json_response)


@app.route('/service-b')
def service_b():
    try:
        response = requests.get(f'http://{backend_host}:{backend_port}/service-b')
        json_response = response.json()
    except Exception as e:
        print("An error occurred:", e)
        json_response = {"message": "Request error"}

    return render_template("service-b.html", active="service-b", data=json_response)


@app.route('/health')
def health():
    return {"status": "UP"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)