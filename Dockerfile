# Use the latest lightweight Python image #
FROM python:3.12-slim

# Environment variables for a cleaner Python environment #
ENV SUPABASE_URL="YOUR_URL" \
    SUPABASE_KEY="YOUR_KEY"

# Set working directory inside the container #
WORKDIR /keystone

# Install system dependencies needed for some Python packages #
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files into the container #
COPY . .

# Install Python dependencies #
RUN pip install --no-cache-dir -r requirements.txt

# Run your main Python script #
CMD ["python", "main.py"]