
# Use an official Python runtime as a parent image
FROM python:3.10-slim

#install bash
# RUN apk add --no-cache bash

# Set the working directory
WORKDIR /appuser

# Install Poetry
RUN pip install poetry

# COPY . .
# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /appuser/

# Install dependencies
RUN poetry install  --no-dev

# Copy the rest of the application code
COPY . /appuser


# Expose port 8000
EXPOSE 8000
# Convert line endings of prestart.sh to Unix format
RUN apt-get update && apt-get install -y dos2unix \
    && dos2unix ./prestart.sh \
    && chmod +x ./prestart.sh

# Run the database initialization script
ENV PYTHONPATH=/appuser

# Command to run the FastAPI server

CMD ["bash", "-c", "poetry run bash ./prestart.sh && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]
