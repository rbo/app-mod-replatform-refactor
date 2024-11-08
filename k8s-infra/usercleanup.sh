#!/bin/bash

read -p "How many user projects do you want to delete? " users

for ((i=1; i<=$users; i=i+1))
do
    USER="user$i"
    echo "Cleaning $USER"

    oc delete project $USER-istio-system
    oc delete project $USER-apps
done