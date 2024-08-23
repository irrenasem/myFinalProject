# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests

# Make port 80 available to the world outside this container
EXPOSE 80

# Run weather_app.py when the container launches
ENTRYPOINT ["python", "weather_app.py"]