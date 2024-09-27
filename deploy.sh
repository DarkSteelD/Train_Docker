#!/bin/bash
podman stop app || true
podman rm app || true
podman run -d --name app -p 5000:5000 my-app-image
