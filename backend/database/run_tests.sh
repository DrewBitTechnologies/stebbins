#!/usr/bin/env bash

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

coverage run -m unittest tests/test_sqlite3.py
coverage report -m

deactivate