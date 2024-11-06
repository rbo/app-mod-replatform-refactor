from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/service-a')
def service_a():
    try:
        response = requests.get('http://localhost:8080/service-a')
        json_response = response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        json_response = {"message": "Request error"}

    return render_template("service-a.html", data=json_response)


@app.route('/service-b')
def service_b():
    try:
        response = requests.get('http://localhost:8080/service-b')
        json_response = response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        json_response = {"message": "Request error"}

    return render_template("service-b.html", data=json_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)