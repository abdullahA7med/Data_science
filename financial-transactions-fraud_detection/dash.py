import streamlit as st
import pandas as pd
import joblib

# with open("model (1).pkl", "rb") as f:
#     pickle.load(f)



st.title("Fraud Detection APP")

model = joblib.load("model (1).pkl")

st.markdown("Type the Transaction details below and use prediction button.")

st.divider()

transaction_type = st.selectbox("Transaction type:" ,["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])

if transaction_type == "CASH_IN":
    transaction_type = 0
elif transaction_type == "CASH_OUT":
    transaction_type = 1
elif transaction_type == "DEBIT":
    transaction_type = 2
elif transaction_type == "PAYMENT":
    transaction_type = 3
elif transaction_type == "TRANSFER":
    transaction_type = 4


amount = st.number_input("Amount:", min_value=0)

old_balance_org = st.number_input("Old Balance (sender):", min_value=0)

new_balance_orig = st.number_input("New Balance (sender):", min_value=0)

old_balance_dest = st.number_input("Old Balance (receiver):", min_value=0)

new_balance_dest = st.number_input("New Balance (receiver):", min_value=0)


st.divider()


if st.button("Prediction"):
    data = {
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [old_balance_org],
        "newbalanceOrig": [new_balance_orig],
        "oldbalanceDest": [old_balance_dest],
        "newbalanceDest": [new_balance_dest]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]

    st.subheader(f"Prediction:'{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraudulent.")
    else:
        st.success("This transaction is not fraudulent.")

