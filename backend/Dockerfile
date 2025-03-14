# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# May want to change 0.0.0.0 to localhost
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
