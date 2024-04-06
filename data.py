import pandas as pd
import glob

# Paths to the folders containing your CSV files
folder_paths = ['wind_power_data/*.csv', 'Grid_data/*.csv']  # Adjust the paths as needed

# Use glob to find all CSV files in both folders
file_names = []
for path in folder_paths:
    file_names.extend(glob.glob(path))

# Assuming the encoding might differ or to handle potential UnicodeDecodeErrors
encoding_type = 'ISO-8859-1'

# Load each file into a DataFrame and store them in a list
dfs = [pd.read_csv(file, encoding=encoding_type) for file in file_names]

# Merge (concatenate) the list of DataFrames into a single DataFrame
merged_data = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_data.to_csv('merged_data.csv', index=False)

# Indicate to the user that the file has been saved
print("Merged data saved to 'merged_data.csv'.")