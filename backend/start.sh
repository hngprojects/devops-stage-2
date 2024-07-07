#!/bin/bash

# Activate the Poetry environment
poetry install --no-dev

# Run any pre-start commands (if needed)
bash ./prestart.sh

# Start the FastAPI application using uvicorn
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000