import pandas as pd
import os

# Folder where CSV files are stored
csv_folder = r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_csv"

all_data = []

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(csv_folder, file)
        df = pd.read_csv(file_path)
        all_data.append(df)

# Combine all dataframes
merged_df = pd.concat(all_data, ignore_index=True)

# Save final merged file
merged_df.to_csv("final_stock_data.csv", index=False)

print("All CSV files merged successfully!")
print("Total Rows:", merged_df.shape[0])
print("Total Columns:", merged_df.shape[1])
