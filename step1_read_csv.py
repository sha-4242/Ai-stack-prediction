#import pandas as pd

#file_path = r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_csv\Sector_data.csv"

#df = pd.read_csv(file_path)

#print("CSV loaded successfully")
#print(df.head())
import pandas as pd

file_path = r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_csv\Sector_data.csv"

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
