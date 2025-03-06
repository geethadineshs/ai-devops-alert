import pandas as pd
from sklearn.ensemble import IsolationForest
import requests

# Load logs from a CSV file (ensure logs.csv exists)
log_data = pd.read_csv("logs.csv")

# Train AI Model for anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
log_data["anomaly"] = model.fit_predict(log_data[["error_code"]])

# Slack Webhook URL (Replace with your actual Webhook URL)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Check for anomalies and send an alert to Slack
if (log_data["anomaly"] == -1).any():
    message = {"text": "🚨 AI Detected Log Anomalies! Please check your system logs."}
    response = requests.post(SLACK_WEBHOOK_URL, json=message)
    
    # Print response status
    if response.status_code == 200:
        print("✅ Alert sent to Slack successfully!")
    else:
        print(f"❌ Failed to send alert. Status Code: {response.status_code}")
