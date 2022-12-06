
# Step 1: Import required packages
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

# Step 2: Load the model
model = pickle.load(open('model/car_price_predictor_model.pkl', 'rb'))

# Step 3: Create the FastAPI instance
app = FastAPI()

# Step 4: Create the Input schema using pydantic.BaseModel
class Input(BaseModel):
    Year: int
    Kms_Driven: int
    Present_Price: float
    Fuel_Type: int
    Transmission: int
    Owner: int

# Step 5: Create routes
@app.get('/')
def read_root():
    return {'msg': 'Car Price Predictor'}

@app.post('/predict')
def predict_price(input: Input):
    data = input.dict()
    data_in = [[
        data['Year'], data['Kms_Driven'], data['Present_Price'], 
        data['Fuel_Type'], data['Transmission'], data['Owner']
        ]]
    prediction = model.predict(data_in)
    return {'prediction': prediction[0]}

# Step 6: Run uvicorn server
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


