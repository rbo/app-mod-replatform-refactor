from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/service-a')
def service_a():
    return render_template("service-a.html")


@app.route('/service-b')
def service_b():
    return render_template("service-b.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)