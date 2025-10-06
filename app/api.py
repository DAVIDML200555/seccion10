from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models.joblib")

models = joblib.load(MODEL_PATH)
app = FastAPI()

class Features(BaseModel):
    Sex: str
    ChestPainType: str
    FastingBS: int
    RestingECG: str
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str

class PredictRequest(BaseModel):
    model_name: str   # <-- Nuevo campo para elegir modelo
    features: Features

@app.post("/predict")
def predict(req: PredictRequest):
    if req.model_name not in models:
        return {"error": f"Modelo '{req.model_name}' no encontrado. Usa uno de: {list(models.keys())}"}
    
    model = models[req.model_name]

    # Convertir features a DataFrame
    input_df = pd.DataFrame([req.features.dict()])
    
    prediction = model.predict(input_df)
    return {"model": req.model_name, "prediction": prediction.tolist()}