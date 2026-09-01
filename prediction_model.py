import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

print("Loading dataset...")

# Load dataset
df = pd.read_csv("stock_price_data.csv")

# Show dataset columns
print("Columns in dataset:")
print(df.columns)

# Remove spaces in ticker names
df["Ticker"] = df["Ticker"].str.strip()

# Show available tickers
print("\nAvailable Tickers:")
print(df["Ticker"].unique())

# Select stock
ticker = "SBIN.NS"

stock_df = df[df["Ticker"] == ticker].copy()

print("\nRows for selected stock:", len(stock_df))

# Convert Date column
stock_df["Date"] = pd.to_datetime(stock_df["Date"])

# Sort by date
stock_df = stock_df.sort_values("Date")

# Create next-day prediction target
stock_df["Target"] = stock_df["Close"].shift(-1)

# Remove rows where target is missing
stock_df = stock_df.dropna(subset=["Target"])

# Select features
X = stock_df[["Open", "High", "Low", "Close", "Volume"]]

# Target variable
y = stock_df["Target"]

print("\nPreparing training data...")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

print("Training Random Forest model...")

# Create model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Model evaluation
error = mean_absolute_error(y_test, predictions)

print("\nModel Trained Successfully!")
print("Mean Absolute Error:", error)

# Predict next day price
latest_data = X.iloc[-1:]
next_day_prediction = model.predict(latest_data)

print("\nPredicted Next Day Closing Price:", next_day_prediction[0])