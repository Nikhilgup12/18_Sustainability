import pandas as pd

# Read both CSV files into DataFrames
merged_data = pd.read_csv("merged_data.csv")
merged_data1 = pd.read_csv("merged_data1.csv")

# Option 1: Concatenate DataFrames (vertically stacking)
merged_all_data = pd.concat([merged_data, merged_data1])

# Option 2: Append DataFrames (adding rows from merged_data1 to merged_data)
# merged_all_data = merged_data.append(merged_data1, ignore_index=True)  # Optional: ignore index resetting

# Print a sample of the merged data (optional)
 # View the first few rows

# Save the final merged data to a new CSV file (optional)
merged_all_data.to_csv("merged_all_data.csv", index=False)  # Optional: remove index column
