# ✈️ AI Flight Delay Predictor

An AI-powered Flight Delay Prediction System built with Python and Machine Learning that predicts whether a flight will be delayed based on airline, weather conditions, departure time, and flight distance.

---

## 🚀 Features

- ✈️ Flight Delay Prediction
- 🤖 Machine Learning Model (Random Forest)
- 🌦️ Weather-Based Analysis
- ⏰ Departure Time Analysis
- 📏 Distance-Based Prediction
- 📊 Probability Score Generation
- ⚠️ Risk Level Classification (Low / Medium / High)
- 🖥️ Simple Command Line Interface (CLI)

---

## 🏗️ Project Structure

```text
flight-delay-predictor-ai/
│
├── app.py
├── train_model.py
├── flights.csv
├── model.pkl
├── airline_encoder.pkl
├── weather_encoder.pkl
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-Learn
- Joblib
- Random Forest Classifier

---

## ▶️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/SamihaCodingKoreHi5/flight-delay-predictor-ai.git
```

### Step 2: Navigate to the Project Folder

```bash
cd flight-delay-predictor-ai
```

### Step 3: Install Required Libraries

```bash
pip install pandas scikit-learn joblib
```

### Step 4: Train the Model

```bash
python train_model.py
```

Expected Output:

```text
Model Trained Successfully!
```

### Step 5: Run the Application

```bash
python app.py
```

---

## 🧪 Sample Input

```text
Airline: Biman
Weather: Rainy
Departure Hour: 9
Distance: 500
```

---

## 📊 Sample Output

```text
==============================
FLIGHT DELAY REPORT
==============================

Prediction: DELAYED
Probability: 82%
Risk Level: High
```

---

## 📷 Screenshots

### Main Input Screen

(Add Screenshot Here)

### Delayed Flight Prediction

(Add Screenshot Here)

### On-Time Flight Prediction

(Add Screenshot Here)

---

## 🧠 How It Works

1. Flight data is loaded from the dataset.
2. Categorical values are encoded.
3. A Random Forest model is trained.
4. User inputs flight information.
5. The model predicts whether the flight will be delayed.
6. A probability score and risk level are generated.

---

## 🎯 Future Improvements

- 🌐 Real-Time Flight Data Integration
- 🌦️ Weather API Integration
- 📊 Interactive Dashboard
- 🧠 Advanced AI Models (XGBoost)
- 📈 Flight Analytics Visualization
- 🚀 Streamlit Web Application

---

## 👩‍💻 Author

Developed by **Samiha Fatima**

If you found this project useful, consider giving it a ⭐ on GitHub.
