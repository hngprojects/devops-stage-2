FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update && apt-get install -y \
    libpq-dev

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create true \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /app/

RUN chmod +x /app/prestart.sh

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "bash", "-c", "/app/prestart.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000"]