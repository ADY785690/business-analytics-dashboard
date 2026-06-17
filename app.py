import streamlit as st
import pandas as pd

st.set_page_config(page_title="Business Analytics Dashboard")

st.title("📊 Business Analytics Dashboard")

revenue = 750000
customers = 250
profit = 180000
leads = 400

conversion_rate = (customers / leads) * 100

col1,col2 = st.columns(2)
col3,col4 = st.columns(2)

col1.metric("Revenue", f"₹{revenue:,}")
col2.metric("Customers", customers)
col3.metric("Profit", f"₹{profit:,}")
col4.metric("Conversion Rate", f"{conversion_rate:.2f}%")

st.divider()

data = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Revenue":[4,5,6,7,8,10],
    "Customers":[50,70,80,100,120,150]
})

st.subheader("Revenue Trend")
st.line_chart(
    data.set_index("Month")["Revenue"]
)

st.subheader("Customer Growth")
st.bar_chart(
    data.set_index("Month")["Customers"]
)

st.subheader("Executive Insights")

st.success("Best Month: June")
st.warning("Lowest Revenue: January")
st.info("Growth Trend: Positive")

csv = data.to_csv(index=False)

st.download_button(
    "Download Analytics Report",
    csv,
    "business_report.csv",
    "text/csv"
)
