#!/bin/bash

docker login
docker build --tag hoseinmaghoul/notification:v1.0.0 . -f Dockerfile
docker push hoseinmaghoul/notification:v1.0.0