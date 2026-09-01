import pandas as pd

# Load dataset
df = pd.read_csv("stock_price_data.csv")

# Drop Adj Close column (it is empty)
df = df.drop(columns=["Adj Close"])

print("Dataset Shape After Cleaning:", df.shape)
print("\nMissing Values:\n")
print(df.isnull().sum())
# Calculate Daily Return
df['Daily_Return'] = df.groupby('Ticker')['Close'].pct_change()

print("\nWith Daily Return:")
print(df[['Ticker', 'Close', 'Daily_Return']].head())
# Remove NaN values (first row of each stock)
df = df.dropna()

# Calculate Average Return and Volatility
summary = df.groupby("Ticker").agg(
    Average_Return=("Daily_Return", "mean"),
    Volatility=("Daily_Return", "std")
).reset_index()

print("\nStock Performance Summary:")
print(summary.sort_values(by="Average_Return", ascending=False))
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

# Scatter plot
plt.scatter(summary["Volatility"], summary["Average_Return"])

# Highlight Top 5 stocks
top5 = summary.sort_values(by="Average_Return", ascending=False).head(5)

for i in range(len(top5)):
    plt.text(top5["Volatility"].iloc[i],
             top5["Average_Return"].iloc[i],
             top5["Ticker"].iloc[i],
             fontsize=9)

plt.xlabel("Volatility (Risk)")
plt.ylabel("Average Daily Return")
plt.title("Risk vs Return of NIFTY Stocks")
plt.grid(True)

plt.show()


