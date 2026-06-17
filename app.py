import streamlit as st
import pandas as pd

st.title("📊 Business Analytics Dashboard")

revenue = st.number_input(
    "Monthly Revenue",
    value=500000
)

customers = st.number_input(
    "Total Customers",
    value=100
)

leads = st.number_input(
    "Total Leads",
    value=250
)

conversion = (customers / leads) * 100

st.metric(
    "Conversion Rate",
    f"{conversion:.2f}%"
)

st.metric(
    "Revenue",
    f"₹{revenue:,.0f}"
)

data = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May"],
    "Revenue": [4,5,6,7,8]
})

st.line_chart(
    data.set_index("Month")
)

st.success("Business KPIs Generated")
