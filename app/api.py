from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os
import sys
import types


main_module = types.ModuleType("__main__")


def dynamic_binarizer(X):
    thresholds = np.mean(X, axis=0)
    return (X > thresholds).astype(int)


main_module.dynamic_binarizer = dynamic_binarizer
sys.modules["__main__"] = main_module

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "models.joblib"))

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
    model_name: str
    features: Features


@app.post("/predict")
def predict(req: PredictRequest):
    if req.model_name not in models:
        available_models = list(models.keys())
        return {
            "error": f"Modelo '{req.model_name}' no encontrado. "
                     f"Usa uno de: {available_models}"
        }
    
    model = models[req.model_name]

    input_df = pd.DataFrame([req.features.dict()])
    
    prediction = model.predict(input_df)
    return {"model": req.model_name, "prediction": prediction.tolist()}