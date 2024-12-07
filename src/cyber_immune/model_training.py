from sklearn.ensemble import IsolationForest
from src.cyber_immune.data_preprocessing import load_data

def train_model():
    X, y, df = load_data()
    # contamination=0.1 veride %10 anomali olduğunu varsayar
    model = IsolationForest(random_state=42, n_estimators=100, contamination=0.1)
    model.fit(X)
    return model

if __name__ == "__main__":
    model = train_model()
    print("Model trained successfully!")
