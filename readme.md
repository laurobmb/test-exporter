# App

podman build -t quay.io/lagomes/test-exporter:v1 .

podman run -p 9000:9000 quay.io/lagomes/test-exporter:v1