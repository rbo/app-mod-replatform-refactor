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

User script `k8s-infra/usersetup.sh` to setup user namespaces.
