# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-openbsd gcc libpq-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (optional, handled by compose)
EXPOSE 8000

# Default command (can override via docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
