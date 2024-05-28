import pandas as pd

# Read data
data = pd.read_csv('Grade2Results.csv')

# Get unique student names
students = data['Names'].unique()

# Reshape data for each student
student_data = []
for student in students:
    student_df = data[data['Names'] == student].set_index('Date')
    student_df = student_df.drop('Names', axis=1).add_prefix(f'{student}_')
    student_data.append(student_df)

# Concatenate reshaped data
progression_data = pd.concat(student_data, axis=1)

# Export to CSV
progression_data.to_csv('progression_data.csv')