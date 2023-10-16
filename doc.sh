#!/bin/bash

#start and clean
docker compose down

rm -f ./python/exel/links.xlsx

docker compose build

docker system prune -f

docker compose up -d

docker image prune -f
