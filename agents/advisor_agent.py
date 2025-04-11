import pickle
import numpy as np

class AdvisorAgent:
    def __init__(self, model_path='models/yield_predictor.py'):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict_yield(self, farm_data):
        features = np.array([
            farm_data['Soil_pH'],
            farm_data['Soil_Moisture'],
            farm_data['Temperature_C'],
            farm_data['Rainfall_mm'],
            farm_data['Fertilizer_Usage_kg'],
            farm_data['Pesticide_Usage_kg']
        ]).reshape(1, -1)
        return self.model.predict(features)[0]
