# Use the official Python image from the Docker Hub
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the server code and protobuffer files to the working directory
COPY . /app

# Install required gRPC dependencies
RUN pip install grpcio
RUN pip install grpcio-tools

# Expose the port on which the REST API server runs
EXPOSE 5000

# Set the environment variable for Python to run the server code
CMD ["python", "end.py"]