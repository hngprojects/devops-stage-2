# Use the latest Python image as the base image
FROM python:latest

# Set the working directory
WORKDIR /backend

# Copy the rest of the application code
COPY . .

RUN pip install poetry

# Install dependencies using Poetry
RUN poetry install

# Make prestart.sh executable
RUN chmod +x ./prestart.sh


# Expose port 8000
EXPOSE 8000

# Start the FastAPI server with wait-for-it script to wait for the database
CMD ["poetry", "run", "bash", "-c", "./prestart.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
