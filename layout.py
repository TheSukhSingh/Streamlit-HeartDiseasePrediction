import warnings 
warnings.filterwarnings('ignore')

import joblib
import streamlit as st



# Load the heart disease prediction model
model = joblib.load('heart_disease_classifier_model.pkl')

# Custom CSS for a unique design
st.markdown(
    """
    <style>
        .prediction-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            margin: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out;
            color: #333; /* Set text color to black */
        }
        .prediction-card:hover {
            transform: scale(1.05);
        }
        .prediction-result {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #333; /* Set text color to black */
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            caret-color: #e50914; /* Set caret color to a visible color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main app content
st.title("Predict Heart Disease")

# User input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ("Male", "Female")) # male= 1 , female = 0
cp = st.number_input("Chest Pain Type", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Resting Blood Pressure", min_value=90, max_value=200, value=120)
chol = st.number_input("Cholesterol", min_value=130, max_value=300, value=220)
fbs = st.number_input("Fasting Blood Sugar", min_value=0, max_value=1, value=0)
restecg = st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=2, value=0)
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=30, max_value=200, value=150)
exang = st.number_input("Exercise-Induced Angina", min_value=0, max_value=1, value=0)
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=4.0, value=0.0)
slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2, value=0)
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
thal = st.number_input("Thallium Stress Test Result", min_value=1, max_value=3, value=1)

if sex == "Male":
    sex = "1"
else:
    sex = "0"



# Prediction button
if st.button("Predict"):
    # Prepare the data for prediction
    data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    
    # Make the prediction
    prediction = model.predict(data)
    
    # Display the prediction result
    st.write("Prediction Result:")

    global wow
    if (prediction[0]== 0):
        wow = 'The Person does not have a Heart Disease'
    else:
        wow = 'The Person has Heart Disease'

    st.markdown(
        f"""
        <div class="prediction-card">
            <p class="prediction-result">{wow}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
