import pandas as pd

file_path = 'Grade2Results.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

csv_file_path = 'Grade2Results.csv'
df.to_csv(csv_file_path, index=False)
