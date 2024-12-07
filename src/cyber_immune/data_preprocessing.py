import pandas as pd

def load_data(filepath="data/sample_logs.csv"):
    df = pd.read_csv(filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Sadeleştirmek için sadece bytes_sent ve status_code'u kullanıyoruz.
    X = df[['bytes_sent', 'status_code']]
    y = df['label']
    return X, y, df
