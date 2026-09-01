import os
import yaml
import pandas as pd

# Folder paths
yaml_folder = r"C:\Users\ADMIN\Desktop\stock_analysis_project(final year)\data_yaml"

output_folder = "../processed_data"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all YAML files
for file in os.listdir(yaml_folder):
    if file.endswith(".yaml") or file.endswith(".yml"):
        file_path = os.path.join(yaml_folder, file)

        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        # Convert to DataFrame
        df = pd.json_normalize(data)

        # Save as CSV
        csv_name = file.replace(".yaml", ".csv").replace(".yml", ".csv")
        df.to_csv(os.path.join(output_folder, csv_name), index=False)

        print(f"{file} converted successfully!")

print("All YAML files converted to CSV!")
