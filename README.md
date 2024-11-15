# Monolith and microservice example

Monolith with endpoints /service-a and /service-b which should be modernized. Strangler pattern is applied and a new microservice created for service-b. Then Service Mesh is used for a Canary Release.

## Develop

Run in app folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

In VSCode: Cmd-Shift-P > Select Python Interpreter > Enter Interpreter Path -> APPFOLDER/.venv/

### Install dependencies

Run in app folder:

```bash
pip install -r requirements.txt
```

### Run app

In app folder:

#### Monolith and Microservice
`python main.py`

#### Webapp

For development:
`FLASK_APP=app/main.py flask run -p 3000`

For producution:
`gunicorn --config gunicorn.conf.py app.main:app`