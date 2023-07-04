#!/bin/bash

docker login
docker build --tag hoseinmaghoul/transaction:v1.0.0 . -f Dockerfile
docker push hoseinmaghoul/transaction:v1.0.0