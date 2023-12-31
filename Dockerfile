# Use the official Python image as the base image
FROM python:3.11.6-alpine3.18

# WORKDIR /app

# COPY . /app

# Copy the application files into the working directory
ADD requirements.txt .
ADD main.py .
ADD aiogram_bot.py .
ADD tradingview.py .

# Install the application dependencies
RUN pip install -r requirements.txt

# EXPOSE 8080

# Define the entry point for the container
CMD ["python", "./main.py"]
