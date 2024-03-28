# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Dash dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Dash application code to the working directory
COPY . .

# Expose the port that the Dash application runs on
EXPOSE 8050

# Command to run the Dash application
CMD ["python3", "main.py"]
