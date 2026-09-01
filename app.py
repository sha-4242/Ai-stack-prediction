import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------

st.set_page_config(page_title="AI Stock Dashboard", layout="wide")

# -------------------------------------------------
# PROFESSIONAL LIGHT UI
# -------------------------------------------------

st.markdown("""
<style>

.stApp{
background-color:#eef2f7;
}

h1{
color:#0f172a;
}

h2{
color:#1e3a8a;
}

h3{
color:#16a34a;
}

[data-testid="metric-container"]{
background-color:white;
border-radius:10px;
padding:15px;
box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.title("📈 AI Stock Market Analysis Dashboard")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

df = pd.read_csv(r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\stock_price_data.csv")

df["Ticker"] = df["Ticker"].str.strip()
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("📊 Stock Selection")

selected_stock = st.sidebar.selectbox(
"Select Stock",
df["Ticker"].unique()
)

# -------------------------------------------------
# 🤖 AI PREDICTION
# -------------------------------------------------

st.header("🤖 AI Stock Price Prediction")

stock_df = df[df["Ticker"] == selected_stock].copy()

stock_df["Target"] = stock_df["Close"].shift(-1)

stock_df = stock_df.dropna(subset=["Target"])

X = stock_df[["Open","High","Low","Close","Volume"]]
y = stock_df["Target"]

st.write("Rows available:", len(stock_df))

if len(stock_df) > 5:

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model = RandomForestRegressor(n_estimators=100)

    model.fit(X_train,y_train)

    latest = X.iloc[-1:]

    prediction = model.predict(latest)[0]

    st.success(f"Predicted Next Day Price: ₹ {prediction:.2f}")

else:

    st.warning("Not enough data for AI prediction")

# -------------------------------------------------
# MARKET SUMMARY
# -------------------------------------------------

latest = df[df["Date"] == df["Date"].max()].copy()

latest["Change"] = latest["Close"] - latest["Open"]

st.header("📊 Market Summary")

col1,col2,col3 = st.columns(3)

col1.metric("Total Stocks", len(latest))
col2.metric("Green Stocks", (latest["Change"]>0).sum())
col3.metric("Red Stocks", (latest["Change"]<0).sum())

# -------------------------------------------------
# CANDLESTICK CHART
# -------------------------------------------------

st.header("📉 Stock Candlestick Chart")

stock_data = df[df["Ticker"] == selected_stock]

fig = go.Figure(data=[go.Candlestick(
    x=stock_data["Date"],
    open=stock_data["Open"],
    high=stock_data["High"],
    low=stock_data["Low"],
    close=stock_data["Close"]
)])

fig.update_layout(
title=f"{selected_stock} Stock Price",
template="plotly_white"
)

st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# TOP GREEN STOCKS
# -------------------------------------------------

st.header("🟢 Top 10 Green Stocks")

green = latest.sort_values("Change",ascending=False).head(10)

st.dataframe(green[["Ticker","Open","Close","Change"]])

# -------------------------------------------------
# TOP RED STOCKS
# -------------------------------------------------

st.header("🔴 Top 10 Red Stocks")

red = latest.sort_values("Change").head(10)

st.dataframe(red[["Ticker","Open","Close","Change"]])

# -------------------------------------------------
# VOLATILITY CHART
# -------------------------------------------------

st.header("📉 Volatility Chart")

volatility = df.groupby("Ticker")["Close"].std().sort_values(ascending=False).head(10)

fig2 = px.bar(
volatility,
title="Most Volatile Stocks",
template="plotly_white"
)

st.plotly_chart(fig2,use_container_width=True)

# -------------------------------------------------
# CORRELATION HEATMAP
# -------------------------------------------------

st.header("🔥 Correlation Heatmap")

pivot = df.pivot_table(index="Date",columns="Ticker",values="Close")

corr = pivot.corr()

fig3,ax = plt.subplots(figsize=(10,6))

sns.heatmap(corr,cmap="coolwarm")

st.pyplot(fig3)

# -------------------------------------------------
# MONTHLY GAINERS & LOSERS
# -------------------------------------------------

st.header("📅 Monthly Gainers & Losers")

df["Month"] = df["Date"].dt.to_period("M")

monthly = df.groupby(["Month","Ticker"])["Close"].mean().reset_index()

latest_month = monthly["Month"].max()

month_data = monthly[monthly["Month"] == latest_month]

gain = month_data.sort_values("Close",ascending=False).head(5)

loss = month_data.sort_values("Close").head(5)

col4,col5 = st.columns(2)

col4.subheader("Top Gainers")
col4.dataframe(gain)

col5.subheader("Top Losers")
col5.dataframe(loss)