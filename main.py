from agents.farmer_agent import FarmerAgent
from agents.advisor_agent import AdvisorAgent
from agents.market_agent import MarketAgent
from agents.weather_agent import WeatherAgent
from agents.sustainability_agent import SustainabilityAgent
from utils.db_handler import DBHandler

def run_system():
    # Example input
    farm_data = {
        'Farm_ID': 'F123',
        'Soil_pH': 6.5,
        'Soil_Moisture': 25.0,
        'Temperature_C': 32.0,
        'Rainfall_mm': 60.0,
        'Crop_Type': 'Wheat',
        'Fertilizer_Usage_kg': 120.0,
        'Pesticide_Usage_kg': 30.0
    }

    # Initialize agents
    farmer = FarmerAgent(farm_data)
    advisor = AdvisorAgent()
    market = MarketAgent()
    weather = WeatherAgent()
    sustainability = SustainabilityAgent()
    db = DBHandler()

    # Gather inputs
    data = farmer.provide_data()
    predicted_yield = advisor.predict_yield(data)
    market_data = market.analyze_market(data['Crop_Type'])
    sustainability_score = sustainability.assess_sustainability(data)
    weather_comment = weather.assess_impact(data['Temperature_C'], data['Rainfall_mm'])

    # Display results
    print(f"Predicted Yield: {predicted_yield:.2f} tons")
    print(f"Market Price: ₹{market_data['price']:.2f}, Demand Index: {market_data['demand']:.2f}")
    print(f"Sustainability Score: {sustainability_score:.2f}")
    print(f"Weather Comment: {weather_comment}")

    # Store results
    db.insert_record((
        data['Farm_ID'],
        data['Crop_Type'],
        predicted_yield,
        market_data['price'],
        market_data['demand'],
        sustainability_score,
        weather_comment
    ))

if __name__ == "__main__":
    run_system()
