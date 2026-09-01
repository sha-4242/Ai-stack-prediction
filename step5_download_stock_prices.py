import pandas as pd
import yfinance as yf

# Load sector data
df = pd.read_csv (r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_csv\Sector_data.csv")


df["Ticker"] = df["Symbol"].apply(lambda x: x.split(":")[1] + ".NS")

all_data = []

for ticker in df["Ticker"]:
    print(f"Downloading {ticker}...")

    stock = yf.download(ticker, period="1y", group_by='column')

    # Flatten multi-index columns if present
    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = stock.columns.get_level_values(0)

    stock.reset_index(inplace=True)
    stock["Ticker"] = ticker

    all_data.append(stock)

# Stack vertically
final_df = pd.concat(all_data, ignore_index=True)

# Keep required columns only
final_df = final_df[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume", "Ticker"]]

# Save
final_df.to_csv("stock_price_data.csv", index=False)

print("✅ All stock price data downloaded correctly!")
