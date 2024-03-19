# Use the official Python image
FROM python:3.10.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app

# Install dependencies
# RUN pip install --upgrade pip
RUN pip install -r req.txt -vvv

# Copy the current directory contents into the container at /app
# COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
