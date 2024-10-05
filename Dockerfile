# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim
LABEL maintainer="Benjamin"

ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_ENV=development

# Run migrations and start the Django development server
# CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
# CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# ENV PATH="/py/bin:$PATH"