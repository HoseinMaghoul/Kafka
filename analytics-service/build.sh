#!/bin/bash

docker login
docker build --tag hoseinmaghoul/analytics:v1.0.0 . -f Dockerfile
docker push hoseinmaghoul/analytics:v1.0.0