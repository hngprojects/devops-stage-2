# Use the official Python image with the desired version
FROM python:3.11

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /application

# Copy pyproject.toml and poetry.lock to the container
COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY . .

# Add Poetry to PATH
ENV PYTHONPATH=/application

# Command to run the backend server
CMD ["sh", "-c", "poetry run bash ./prestart.sh && poetry run uvicorn app.main:app --host 0.0.0.0"]
