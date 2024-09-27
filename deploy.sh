podman stop app || true
podman rm app || true
podman pull docker.io/your-dockerhub-username/your-image-name
podman run -d --name app -p 5000:5000 docker.io/your-dockerhub-username/your-image-name