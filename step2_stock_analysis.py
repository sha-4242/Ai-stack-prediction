# Step 1: Import pandas
import pandas as pd

# Step 2: Load one stock CSV file
# (Change the filename if needed)
file_path = r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_csv\Sector_data.csv"


df = pd.read_csv(file_path)

# Step 3: Show first 5 rows
print("First 5 rows:")
print(df.head())

# Step 4: Show column names
print("\nColumns in dataset:")
print(df.columns)
# Step 1: Import pandas
import pandas as pd

# Step 2: Load one stock CSV file
# (Change the filename if needed)
file_path = r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_csv\Sector_data.csv"


df = pd.read_csv(file_path)

# Step 3: Show first 5 rows
print("First 5 rows:")
print(df.head())

# Step 4: Show column names
print("\nColumns in dataset:")
print(df.columns)
