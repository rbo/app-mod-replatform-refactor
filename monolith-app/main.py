from bottle import route, run


@route('/')
def index():
    return {"message": "Hello world"}


@route("/service-a")
def service_a():
    return {"message": "Hello from Service a"}


@route("/service-b")
def service_b():
    return {"message": "Hello from Service b"}


@route("/health/readiness")
def readiness():
    return {"message": "Ready"}


@route("/health/liveness")
def liveness():
    return {"message": "Ready"}


run(host='0.0.0.0', port=8080)
