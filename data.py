import pandas as pd
import glob

folder_paths = ['wind_power_data/*.csv', 'Grid_data/*.csv'] 


file_names = []
for path in folder_paths:
    file_names.extend(glob.glob(path))


encoding_type = 'ISO-8859-1'


dfs = [pd.read_csv(file, encoding=encoding_type) for file in file_names]


merged_data = pd.concat(dfs, ignore_index=True)


print(merged_data)
