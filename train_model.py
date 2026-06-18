import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("flights.csv")

# Encode categorical columns
airline_encoder = LabelEncoder()
weather_encoder = LabelEncoder()

df["Airline"] = airline_encoder.fit_transform(df["Airline"])
df["Weather"] = weather_encoder.fit_transform(df["Weather"])

X = df[["Airline", "Weather", "Departure_Hour", "Distance"]]
y = df["Delay"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save everything
joblib.dump(model, "model.pkl")
joblib.dump(airline_encoder, "airline_encoder.pkl")
joblib.dump(weather_encoder, "weather_encoder.pkl")

print("Model Trained Successfully!")
