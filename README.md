# Monolith and microservice example

Monolith with endpoints /service-a and /service-b which should be modernized. Strangler pattern is applied and a new microservice created for service-b. Then Service Mesh is used for a Canary Release.

This is what we want to achieve:

![App modernization with OpenShift Virt, Container Platform and Service Mesh](assets/app_mod.png)

## Instructions

You'll find instructions how to setup the infrastructure and how to run the lab here:

* [Infrastructure prep guide](README_INFRA_PREPARE.md)
* [Lab guide](README_LAB_INSTRUCTION.md)

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
`python main.py`

#### Webapp

`npm run dev`

#### Microservice

`quarkus dev`