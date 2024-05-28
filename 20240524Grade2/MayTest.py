import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data (adjust the file path as necessary)
df = pd.read_excel('MayResults.xlsx', sheet_name='Sheet1')

# Calculate descriptive statistics
descriptive_stats = df.describe()
print(descriptive_stats)

# Plotting
plt.figure(figsize=(14, 8))

# Box plot for each category
plt.subplot(2, 1, 1)
sns.boxplot(data=df.iloc[:, 1:-1])
plt.title('Box Plot of Scores by Category')
plt.xticks(rotation=45)

# Bar plot for mean scores by category
plt.subplot(2, 1, 2)
df.iloc[:, 1:-1].mean().plot(kind='bar')
plt.title('Mean Scores by Category')
plt.ylabel('Mean Score')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
