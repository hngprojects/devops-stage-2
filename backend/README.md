# Backend - FastAPI with PostgreSQL

This directory contains the backend of the application built with FastAPI and a PostgreSQL database.

## Prerequisites
- Python 3.8 or higher
- Poetry (for dependency management)
- PostgreSQL (ensure the database server is running)

### Installing Poetry

To install Poetry, follow these steps:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to your PATH (if not automatically added):
```sh
# Example for Bash shell
export PATH="$HOME/.poetry/bin:$PATH"
```

## Setup Instructions

 **Navigate to the backend directory**:
    ```sh
    cd backend
    ```

 **Install dependencies using Poetry**:
    ```sh
    poetry install
    ```

 **Setup PostgreSQL**

**Follow these instructions to install PostgreSQL on Linux and configure a user named app with password changethis123 and a database named app. Give all permissions of the app database to the app user.**

## Install PostgreSQL on Linux (example for Ubuntu):

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

## Switch to the PostgreSQL user and access the PostgreSQL shell:

```bash
sudo -i -u postgres
psql
```

## Create a user app with password changethis123:

```sql
-- Create the database if it doesn't exist
CREATE DATABASE app;

-- Create the user if it doesn't exist, or update the password if it does
DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT
      FROM   pg_catalog.pg_user
      WHERE  usename = 'app') THEN

      CREATE USER app WITH PASSWORD 'changethis123';
   ELSE
      ALTER USER app WITH PASSWORD 'changethis123';
   END IF;
END
$do$;

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE app TO app;
```

## Exit the PostgreSQL shell and switch back to your regular user.

```bash
exit
```

## Set database credentials

## Edit the PostgreSQL environment variables located in the .env file. Make sure the credentials match the database credentials you just created.

```bash
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=app
POSTGRES_USER=app
POSTGRES_PASSWORD=changethis123
```

## Seed the database with the necessary tables and initial data:
    ```sh
    poetry run bash ./prestart.sh
    ```

## start the backend server:
    ```sh
    poetry run uvicorn app.main:app --reload
    ```

## Update configuration:
   Ensure you update the necessary configurations in the `.env` file, particularly the database configuration.
