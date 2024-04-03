# Use the official Python image as the base image
FROM python:3.8
MAINTAINER sathwik
# Set the working directory in the container
WORKDIR /app
# Copy the application files into the working directory
COPY . /app
# Install the application dependencies
RUN pip install -r requirements.txt
# Expose port 80
EXPOSE 80
# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
