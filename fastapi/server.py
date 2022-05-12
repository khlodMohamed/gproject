from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import load_models
from typing import List


# Here we load all the models we need for the project
models = load_models()


class Input(BaseModel):
    input_list: List[float] = []

app = FastAPI()


@app.get("/")
async def root():
    return {"Response": "Welcome to doctor Helper API"}

@app.post("/{model}")
async def get_predictions(model: str, input_list: Input):
    if model in models:
        prediction_prob = models[model].predict_proba([input_list.input_list]).max() * 100
        prediction_class = models[model].predict([input_list.input_list])[0]
        return {"PredictionClass": str(prediction_class), "Probability": str(prediction_prob)}
    else:
        raise HTTPException(status_code=404, detail="Model not found")