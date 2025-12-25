from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model=joblib.load("titanic.pkl")

class Passanger (BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

@app.post("/predict")
def predict_status(passanger:Passanger):
    data=pd.DataFrame([passanger.dict()])
    prediction=model.predict(data)
    result = int(prediction[0])
    if result==1:
        return{"status":"Alive","Prediction":1}
    else :
        return{"status":"deid","Prediction":0}


@app.get('/')
def home():
    return {"message": "Titanic API is running!"}

