import json
import pickle

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Load model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))


@app.post("/diabetes_prediction")
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dicionary = json.loads(input_data)

    preg = input_dicionary["Pregnancies"]
    glu = input_dicionary["Glucose"]
    bp = input_dicionary["BloodPressure"]
    skin = input_dicionary["SkinThickness"]
    insulin = input_dicionary["Insulin"]
    bmi = input_dicionary["BMI"]
    dpf = input_dicionary["DiabetesPedigreeFunction"]
    age = input_dicionary["Age"]

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return "Esta pessoa não tem diabetes!"

    else:
        return "Esta pessoa tem diabetes!"
