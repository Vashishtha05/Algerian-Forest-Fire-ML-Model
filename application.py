import streamlit as st
import pickle
import numpy as np

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="FWI Prediction Dashboard",
    page_icon="🔥",
    layout="wide"
)

# ---------------------------------------------------
# Load Model + Scaler
# ---------------------------------------------------
ridge_model = pickle.load(open(r"C:\CP\ML\25 ML Project\models\ridge.pkl", "rb"))
standard_scalar = pickle.load(open(r"C:\CP\ML\25 ML Project\models\scaler.pkl", "rb"))

# ---------------------------------------------------
# Advanced Styling
# ---------------------------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#0f172a,#020617);
    color: white;
}

/* Title */
.title {
    font-size:42px;
    font-weight:700;
    text-align:center;
    margin-bottom:10px;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(14px);
    border-radius:18px;
    padding:30px;
    box-shadow:0 8px 25px rgba(0,0,0,0.4);
}

/* Result Card */
.result-box {
    text-align:center;
    padding:25px;
    font-size:28px;
    border-radius:15px;
    background: linear-gradient(90deg,#ff4b4b,#ff784b);
    color:white;
    font-weight:bold;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color:#020617;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown('<div class="title">🔥 Fire Weather Index Prediction</div>', unsafe_allow_html=True)
st.write("Machine Learning dashboard for predicting wildfire risk using Ridge Regression.")

# ---------------------------------------------------
# Sidebar Inputs (Professional Dashboard Layout)
# ---------------------------------------------------
st.sidebar.header("Input Parameters")

Temperature = st.sidebar.number_input("Temperature")
RH = st.sidebar.number_input("RH")
Ws = st.sidebar.number_input("Wind Speed (Ws)")
Rain = st.sidebar.number_input("Rain")
FFMC = st.sidebar.number_input("FFMC")
DMC = st.sidebar.number_input("DMC")
ISI = st.sidebar.number_input("ISI")
Classes = st.sidebar.number_input("Classes")
Region = st.sidebar.number_input("Region")

predict = st.sidebar.button("🔥 Predict FWI")

# ---------------------------------------------------
# Main Layout
# ---------------------------------------------------
col1, col2 = st.columns([2,1])

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("Model Overview")

    st.write("""
    This dashboard predicts **Fire Weather Index (FWI)** using environmental variables.
    
    Model Used:
    - Ridge Regression
    - StandardScaler preprocessing
    """)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("Live Status")
    st.metric(label="Model", value="Ridge Regression")
    st.metric(label="Inputs", value="9 Features")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Prediction Section
# ---------------------------------------------------
st.write("")
result_placeholder = st.empty()

if predict:

    input_data = np.array([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
    scaled_data = standard_scalar.transform(input_data)
    prediction = ridge_model.predict(scaled_data)[0]

    result_placeholder.markdown(
        f'<div class="result-box">Predicted FWI: {prediction:.3f}</div>',
        unsafe_allow_html=True
    )
