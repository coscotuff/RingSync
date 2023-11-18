# Use the official Python image from the Docker Hub
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the server code to the working directory
COPY end.py /app

# Install required dependencies
RUN pip install flask

# Expose the port on which the REST API server runs
EXPOSE 5000

# Set the environment variable for Python to run the server code
CMD ["python", "end.py"]