import streamlit as st # type: ignore
import pandas as pd
import joblib

model  =joblib.load("C:/Users/varis/OneDrive/Desktop/genai/FraudDetection/fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction Tool")
st.markdown("Please enter the transaction details and press the predict button")
st.divider()
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER","CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount", min_value =0.00,value =1000.00)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value =0.00,value =10000.00)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value =0.00,value =9000.00)
oldbalanceDest = st.number_input("Old Balance (Reciever)", min_value =0.00,value =0.00)
newbalanceDest = st.number_input("New Balance (Reciever)", min_value =0.00,value =0.00)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest

    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"prediction: '{int(prediction)}")

    if prediction ==1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not fraud")


