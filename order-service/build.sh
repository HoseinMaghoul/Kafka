#!/bin/bash

docker login
docker build --tag hoseinmaghoul/orders:v1.0.0 . -f Dockerfile
docker push hoseinmaghoul/orders:v1.0.0