import pandas as pd
from datetime import datetime

def load_data(filepath="data/sample_logs.csv"):
    df = pd.read_csv(filepath)
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Extract numeric features (for simplicity, use just bytes_sent and status_code)
    X = df[['bytes_sent', 'status_code']]
    y = df['label']
    return X, y, df
