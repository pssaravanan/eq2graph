# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy Poetry files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi

# Copy application code
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Start FastAPI app using uvicorn via Poetry
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]