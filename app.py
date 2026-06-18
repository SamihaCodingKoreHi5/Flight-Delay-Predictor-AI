import joblib

# Load model and encoders
model = joblib.load("model.pkl")
airline_encoder = joblib.load("airline_encoder.pkl")
weather_encoder = joblib.load("weather_encoder.pkl")

print("\n===== AI FLIGHT DELAY PREDICTOR =====\n")

# User Input
airline = input("Airline: ")
weather = input("Weather (Clear/Rainy/Fog/Storm): ")
departure_hour = int(input("Departure Hour (0-23): "))
distance = int(input("Distance (km): "))

try:
    airline_encoded = airline_encoder.transform([airline])[0]
    weather_encoded = weather_encoder.transform([weather])[0]

    prediction = model.predict(
        [[airline_encoded, weather_encoded, departure_hour, distance]]
    )[0]

    probability = model.predict_proba(
        [[airline_encoded, weather_encoded, departure_hour, distance]]
    )[0]

    delay_probability = round(max(probability) * 100)

    if prediction == 1:
        result = "DELAYED"
    else:
        result = "ON TIME"

    if delay_probability >= 80:
        risk = "High"
    elif delay_probability >= 50:
        risk = "Medium"
    else:
        risk = "Low"

    print("\n==============================")
    print("FLIGHT DELAY REPORT")
    print("==============================")

    print(f"\nPrediction: {result}")
    print(f"Probability: {delay_probability}%")
    print(f"Risk Level: {risk}")

except ValueError:
    print("\nUnknown Airline or Weather Type!")
