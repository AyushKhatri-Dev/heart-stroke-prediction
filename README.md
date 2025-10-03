# Heart Stroke Prediction ❤️¸

A machine learning web application built with Streamlit that predicts the risk of heart disease based on various health parameters using K-Nearest Neighbors (KNN) algorithm.

## đŸ"‹ Features

- Interactive web interface for easy input
- Real-time heart disease risk prediction
- Uses KNN machine learning model
- Standardized feature scaling for accurate predictions
- User-friendly sliders and dropdowns for data entry

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning
- **Joblib** - Model serialization

## 📊 Input Parameters

The model takes the following inputs:

1. **Age** (18-100 years)
2. **Sex** (M/F)
3. **Chest Pain Type** (ATA, NAP, TA, ASY)
4. **Resting Blood Pressure** (80-200 mm Hg)
5. **Cholesterol** (100-600 mg/dL)
6. **Fasting Blood Sugar** (>120 mg/dL: Yes/No)
7. **Resting ECG** (Normal, ST, LVH)
8. **Max Heart Rate** (60-220 bpm)
9. **Exercise-Induced Angina** (Y/N)
10. **Oldpeak** (ST Depression: 0.0-6.0)
11. **ST Slope** (Up, Flat, Down)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/heart-stroke-prediction.git
cd heart-stroke-prediction

2.Install required packages:
pip install -r requirements.txt

3. Run the application:
streamlit run app.py


đź"‚ Project Structure
heart-stroke-prediction/
│
├── app.py                 # Main Streamlit application
├── KNN_heart.pkl          # Trained KNN model
├── scaler.pkl             # Feature scaler
├── columns.pkl            # Expected column names
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
