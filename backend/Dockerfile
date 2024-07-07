# Use an official Python runtime as a parent image
FROM python:3.10.0-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev  # for PostgreSQL dependencies

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        libpq-dev \
        python3 \
        python3-pip \
        python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry using a Python script
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the environment variable for Poetry
ENV PATH="/root/.local/bin:$PATH"

# Verify Poetry installation
RUN poetry --version


WORKDIR /app

# Copy only the requirements to cache them in the Docker layer
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

# Copy the rest of your application code into the container.
COPY . .

COPY start.sh .


RUN chmod +x start.sh

CMD ["./start.sh"]