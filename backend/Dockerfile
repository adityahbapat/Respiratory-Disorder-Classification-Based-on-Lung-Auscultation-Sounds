# Use the official Python 3.10.6 image
FROM python:3.9-slim


# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install core dependencies.
RUN apt-get update && apt-get install libsndfile1-dev -y

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code from the local 'backend' folder to /app in the container
COPY . .

# Expose the port your app run
EXPOSE 5000

# Set the command to run the app
CMD ["python", "app.py"]
