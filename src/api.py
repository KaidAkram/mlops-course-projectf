from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI()

# --- LOAD THE TRAINED MODEL ---
# This checks if your 'train.py' actually created the file
model_path = "rules_model.pkl"

if os.path.exists(model_path):
    try:
        rules = joblib.load(model_path)
        status = "Model Loaded Successfully"
        rule_count = len(rules)
    except:
        rules = pd.DataFrame()
        status = "Error Loading Model"
        rule_count = 0
else:
    rules = pd.DataFrame()
    status = "Model File Not Found (Did you run train.py?)"
    rule_count = 0

# --- API ENDPOINTS ---

@app.get("/")
def health_check():
    """Checks if the server is running and model is ready."""
    return {
        "system_status": "Online",
        "model_status": status,
        "total_rules_available": rule_count
    }

@app.post("/recommend")
def recommend(symptom: str):
    """
    Simulates a recommendation. 
    Real logic would look up 'symptom' in the 'rules' dataframe.
    """
    return {
        "input_symptom": symptom,
        "recommendation": "Consult a Doctor (Simulated Rule)",
        "confidence": 0.85,
        "note": "This is a demonstration for MLOps Project"
    }
