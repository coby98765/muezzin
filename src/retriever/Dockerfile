
# --- Stage 1: Build dependencies in a virtual environment ---
FROM python:3.12-slim AS builder

WORKDIR /app

# Create a virtual environment to isolate dependencies
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 2: Build the final, lightweight image ---
FROM python:3.12-slim

WORKDIR /app

# Copy the virtual environment with installed dependencies from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Set environment variables to use the virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Declare ENV var's
ENV DB_NAME=""
ENV DB_HOST=""
ENV TOPIC=""
ENV KAFKA_HOST=""

# Copy the application source code
COPY . /app/
WORKDIR /app
# Command to run the Uvicorn server
CMD ["python", "main.py"]