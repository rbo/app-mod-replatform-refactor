import os

port = int(os.environ.get("PORT", default=8080))


async def app(scope, receive, send):
    assert scope["type"] == "http"

    match scope["path"]:
        case "/":
            text, status = "Hello from vm-app\n", 200
        case "/health":
            text, status =  "UP\n", 200
        case _:
            text, status = "Page not found\n", 404

    response_headers = [(b"content-type", b"text/plain; charset=utf-8")]
    await send({"type": "http.response.start", "status": status, "headers": response_headers})
    await send({"type": "http.response.body", "body": text.encode("UTF-8")})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, proxy_headers=True, server_header=False, access_log=False)