#!/bin/bash

read -p "How many user projects do you want to delete? " users

for ((i=1; i<=$users; i=i+1))
do
    USER="user$i"
    echo "Cleaning $USER"

    oc delete project mtv-$USER
    oc delete project oadp-$USER
    oc delete project showroom-$USER
    oc delete project vmimported-$USER
done