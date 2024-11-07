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

## Service Mesh preparation

Install in order: 

* **Red Hat OpenShift distributed tracing platform**
Namespace: openshift-distributed-tracing
* **Kiali**
Namespace: openshift-operators
* **Red Hat OpenShift Service Mesh**
Namespace: openshift-operators

Then:

* Create "istio-system" namespace and then insdie the ServiceMeshControlPlane (kubernetes/controlplane.yml)
    ```sh
    oc apply -f k8s/infra/controlplane.yml
    ```
* When the control plane is up and running, create the ServiceMeshMemberRoll (kubernetes/memberroll.yml) inside "istio-system" for your apps namespace
    ```sh
    oc apply -f k8s/infra/memberroll.yml
    ```
