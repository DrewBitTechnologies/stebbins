#!/usr/bin/env bash

if [[ $1 == "-p" ]]; then
    docker compose -f docker-compose.yaml up --build
else
    docker compose -f docker-compose-dev.yaml up --build
fi