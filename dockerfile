# Use the official Python image as the base image
FROM python:3.10-slim

# Set environment variables to prevent writing .pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Define build-time arguments (for .env variables)
ARG WORKERS
ARG PORT
ARG HOST

# Set runtime environment variables based on build arguments
ENV WORKERS=$WORKERS \
    PORT=$PORT \
    HOST=$HOST

# Expose the specified port
EXPOSE $PORT

# Run the Flask app using Hypercorn
CMD ["python", "app.py"]
