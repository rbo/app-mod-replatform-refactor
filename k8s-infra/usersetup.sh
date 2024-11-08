#!/bin/bash

read -p "How many users do you want to configure? " users

create_servicemesh() {
cat <<EOF | kubectl apply -f -
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: $1-istio-system
spec:
  version: v2.6
  tracing:
    type: None
    sampling: 10000
  addons:
    kiali:
      enabled: true
      name: kiali
    grafana:
      enabled: false
---
kind: ServiceMeshMemberRoll
apiVersion: maistra.io/v1
metadata:
  name: default
  namespace: $1-istio-system
spec:
  members:
    - $1-apps
EOF
}

for ((i=1; i<=$users; i=i+1))
do
    USER="user$i"
    echo "Setting up $USER"

    oc new-project $USER-istio-system
    oc adm policy add-role-to-user edit $USER -n $USER-istio-system

    oc new-project $USER-apps
    oc adm policy add-role-to-user edit $USER -n $USER-apps

    create_servicemesh $USER

    echo "Setup for $USER done"
done
