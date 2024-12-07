Cyber-Immune

A next-generation adaptive cybersecurity framework prototype that leverages AI-based anomaly detection. The goal is to build a system capable of identifying unusual behavior in network traffic and, in the future, integrate blockchain-based trust scoring, quantum-resistant cryptography, and other advanced features.

This MVP (Minimum Viable Product) focuses on detecting anomalies using an Isolation Forest model and providing a simple REST API endpoint for on-demand evaluations.
Key Features

    Modular Architecture: Organized under src/cyber_immune for clear code separation and scalability.
    AI-Powered Anomaly Detection: Utilizes Isolation Forest (scikit-learn) to identify suspicious activity.
    RESTful API with FastAPI: A /detect endpoint allows external queries to classify incoming requests as normal or anomalous.
    Extensible & Open-Source: Built with open-source technologies and designed for future enhancements such as blockchain integration, quantum-resistant cryptography, and automated response mechanisms.

Project Structure

Cyber-Immune/
├─ data/
│  └─ sample_logs.csv          # Sample log data for training
├─ src/
│  ├─ __init__.py
│  └─ cyber_immune/
│     ├─ __init__.py
│     ├─ api.py                # Defines the FastAPI app and endpoints
│     ├─ anomaly_detection.py  # Logic to predict anomalies using the model
│     ├─ data_preprocessing.py # Data loading and preprocessing
│     └─ model_training.py     # Model training script (Isolation Forest)
├─ tests/
│  ├─ __init__.py
│  ├─ test_data.py             # Basic test for data loading
│  └─ test_model.py            # Future tests for the model
├─ requirements.txt            # Dependencies
└─ README.md

Requirements

    Python 3.9+
    pip

Install dependencies:

pip install -r requirements.txt

Quick Start

    Clone the Repository:

git clone https://github.com/your-username/Cyber-Immune.git
cd Cyber-Immune

Set Up Python Dependencies:

pip install -r requirements.txt

Run the Application:

uvicorn src.cyber_immune.api:app --reload

The server starts at http://127.0.0.1:8000.

Test the Endpoint: Use curl or a tool like Postman:

    curl.exe -X POST "http://127.0.0.1:8000/detect" ^
    -H "Content-Type: application/json" ^
    -d "{\"bytes_sent\":120000, \"status_code\":200}"

    You should receive a JSON response indicating "anomalous" or "normal".

Usage

    The /detect endpoint expects a JSON payload with the fields bytes_sent (int) and status_code (int):

{
  "bytes_sent": 1500,
  "status_code": 200
}

It returns:

{
  "result": "normal"
}

or

    {
      "result": "anomalous"
    }

Testing

Run tests with pytest:

pytest

This will run the available tests under tests/ to ensure that data loading and other components are working as intended.
Roadmap

    Short Term:
        Persist model to disk to avoid re-training on each startup.
        Improve feature engineering and anomaly detection accuracy.
        Add more robust test coverage.

    Long Term:
        Integrate blockchain-based trust scoring.
        Implement quantum-resistant cryptographic primitives.
        Develop a fully autonomous "immune system" response mechanism for cybersecurity incidents.

Contributing

Contributions are welcome! To contribute:

    Fork the repository.
    Create a new branch for your feature or bugfix.
    Commit and push your changes.
    Open a pull request detailing the modifications and reasoning.

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as permitted by the license.