import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np

st.set_page_config(
    page_title="Stock Market Intelligence Dashboard",
    layout="wide"
)

st.title("📈 Stock Market Intelligence Dashboard")
st.markdown("Professional Stock Analysis using Yahoo Finance")

# Sidebar
st.sidebar.header("Analysis Settings")

stock = st.sidebar.selectbox(
    "Select Stock",
    [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ITC.NS",
        "SBIN.NS"
    ]
)

start_date = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2023-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("today")
)

if st.sidebar.button("Analyze Stock"):

    with st.spinner("Fetching market data..."):

        data = yf.download(
            stock,
            start=start_date,
            end=end_date,
            progress=False
        )

    if data.empty:
        st.error("No data found for selected stock and date range.")
    else:

        st.subheader(f"📊 Analysis for {stock}")

        current_price = float(data["Close"].iloc[-1])
        highest_price = float(data["High"].max())
        lowest_price = float(data["Low"].min())

        returns = data["Close"].pct_change().dropna()
        volatility = float(returns.std() * np.sqrt(252) * 100)

        sma50 = data["Close"].rolling(window=50).mean()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Current Price",
            f"₹{current_price:.2f}"
        )

        col2.metric(
            "Highest Price",
            f"₹{highest_price:.2f}"
        )

        col3.metric(
            "Lowest Price",
            f"₹{lowest_price:.2f}"
        )

        st.subheader("📈 Closing Price Trend")
        st.line_chart(data["Close"])

        st.subheader("📉 50-Day Moving Average")

        chart_df = pd.DataFrame({
            "Close Price": data["Close"],
            "50 Day MA": sma50
        })

        st.line_chart(chart_df)

        st.subheader("⚡ Risk Analysis")

        st.metric(
            "Annualized Volatility",
            f"{volatility:.2f}%"
        )

        st.subheader("💰 Investment Simulation")

        investment = st.number_input(
            "Enter Investment Amount (₹)",
            min_value=1000,
            value=10000,
            step=1000
        )

        shares = investment / current_price
        portfolio_value = shares * current_price

        st.success(
            f"Estimated Holdings: {shares:.2f} Shares"
        )

        st.info(
            f"Current Portfolio Value: ₹{portfolio_value:,.2f}"
        )

        st.subheader("📋 Latest Market Data")
        st.dataframe(data.tail())

else:
    st.info("👈 Select stock and click 'Analyze Stock'")

st.markdown("---")

st.markdown("""
## 🚀 Features

✅ Real-Time Stock Data using Yahoo Finance

✅ Interactive Stock Selection

✅ Date Range Analysis

✅ KPI Dashboard

✅ Moving Average Analysis

✅ Volatility Analysis

✅ Investment Simulation

✅ Professional Visualizations

✅ Financial Analytics Dashboard
""")
