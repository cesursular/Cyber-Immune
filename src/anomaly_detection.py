import joblib
from src.model_training import train_model

# İlk etapta model her seferinde yeniden eğitilebilir, daha sonra modele kaydetme eklenecek.
model = train_model()

def predict_anomaly(data_dict):
    """
    data_dict: {'bytes_sent': int, 'status_code': int}
    Returns: 'normal' or 'anomalous'
    """
    X = [[data_dict['bytes_sent'], data_dict['status_code']]]
    pred = model.predict(X)
    return 'anomalous' if pred[0] == -1 else 'normal'
