FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN poetry run bash ./prestart.sh

EXPOSE 8000

CMD [ "poetry", "run", "uvicorn", "app.main:app", "--reload --host 0.0.0.0 --port 8000"]



# FROM python:3.11-slim

# WORKDIR /app

# RUN apt-get update && apt-get install -y curl && \
#     curl -sSL https://install.python-poetry.org | python3 -

# ENV PATH="/root/.local/bin:${PATH}"

# COPY poetry.lock pyproject.toml ./

# RUN poetry install

# COPY . .

# RUN poetry run bash ./prestart.sh   

# EXPOSE 8000

# CMD ["poetry", "run", "uvicorn", "app.main:app", "--reload",]