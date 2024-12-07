from fastapi import FastAPI
from pydantic import BaseModel
from src.anomaly_detection import predict_anomaly

app = FastAPI()

class LogEntry(BaseModel):
    bytes_sent: int
    status_code: int

@app.post("/detect")
def detect(entry: LogEntry):
    result = predict_anomaly(entry.dict())
    return {"result": result}
