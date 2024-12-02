#!/bin/bash

echo "-- Building web-app"
podman build -t app-mod-web-app:latest web-app
echo "-- Tagging web-app"
podman tag app-mod-web-app:latest quay.io/nlembers/app-mod-web-app:latest
echo "-- Pushing web-app"
podman push quay.io/nlembers/app-mod-web-app:latest
echo -e "-- Done\n"

echo "-- Building microservice-app"
podman build -t app-mod-microservice-app:latest microservice-app
echo "-- Tagging microservice-app"
podman tag app-mod-microservice-app:latest quay.io/nlembers/app-mod-microservice-app:latest
echo "-- Pushing microservice-app"
podman push quay.io/nlembers/app-mod-microservice-app:latest
echo -e "-- Done\n"