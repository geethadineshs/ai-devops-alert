from flask import Flask, request
import logging
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Log file path
LOG_FILE = "logs.csv"

# Ensure the CSV file has a header row
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "error_code", "message"])

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    log_request(200, "Home page accessed")
    return "Hello, DevOps + AI!"

@app.route("/error")
def error():
    app.logger.error("An error occurred!")
    log_request(500, "An error occurred")
    return "Error triggered!", 500

def log_request(error_code, message):
    """Function to log request data into logs.csv"""
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), error_code, message])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
