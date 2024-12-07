from src.cyber_immune.model_training import train_model

# Şimdilik model her seferinde yeniden eğitiliyor. İleride modeli diske kaydedip load edebiliriz.
model = train_model()

def predict_anomaly(data_dict):
    # data_dict = {'bytes_sent': int, 'status_code': int}
    X = [[data_dict['bytes_sent'], data_dict['status_code']]]
    pred = model.predict(X)
    # Isolation Forest: -1 = anomalous, 1 = normal
    return 'anomalous' if pred[0] == -1 else 'normal'
