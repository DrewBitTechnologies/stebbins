#!/usr/bin/env bash

if [[ $1 == "-p" ]]; then
    docker compose -f docker-compose.yaml up -d
else
    docker compose -f docker-compose-dev.yaml up -d
fi