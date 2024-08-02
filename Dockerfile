# Use the slim variant of Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update the package list and install any necessary system packages
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    # Add any necessary packages here (e.g., build-essential, gcc, etc.)
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD ["python", "app.py"]
