# Use the official Python image with the desired version
FROM python:3.11-slim

# Install system dependencies and build tools
RUN apt-get update && \
    apt-get install -y curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application code to the container
COPY . /app

# Ensure the application directory is in the Python path
ENV PYTHONPATH=/app

# Ensure the prestart.sh script is executable
RUN chmod +x ./prestart.sh

# Expose the application port
EXPOSE 8000

# Command to run the backend server
CMD poetry run bash ./prestart.sh;poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

