# Use a lightweight base image
FROM python:3.10-slim

# Updating libraries
RUN apt-get update && apt-get install -y \
   libpq-dev

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy project files
COPY . .

# Install dependencies (including poetry)
RUN poetry config virtualenvs.create true \
&& poetry install --no-dev --no-interaction --no-ansi

RUN chmod +x /app/prestart.sh
EXPOSE 8000
ENTRYPOINT ["poetry", "run", "bash", "-c", "/app/prestart.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000"]