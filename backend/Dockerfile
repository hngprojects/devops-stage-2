# Use an official Python runtime as a parent image
FROM python:3.10.0-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        curl \
        libpq-dev  # Example: PostgreSQL dependencies
RUN rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set Poetry's bin directory in the PATH
ENV PATH="/root/.local/bin:$PATH"

# Verify Poetry installation
RUN poetry --version

# Install psycopg2-binary
RUN pip install psycopg2-binary

# Set the working directory in the container
WORKDIR /app

# Copy only the dependencies definition files to cache them in Docker layer
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY . .

RUN chmod +x prestart.sh

EXPOSE 8000

# Command to run prestart.sh and the application using Poetry
CMD ["bash", "-c", "poetry run bash ./prestart.sh && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]