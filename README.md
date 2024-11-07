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

#### Monolith
`fastapi run app/main.py`

#### Microservice
`python main.py`
