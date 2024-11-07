# Setup and prepare

## OpenShift

Order "Experience OpenShift Virtualization Roadshow" in demo catalog or setup OpenShift with Virtualization.

## Service Mesh

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
