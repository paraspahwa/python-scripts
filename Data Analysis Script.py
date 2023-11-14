# Analyze and visualize data using pandas and matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'data.csv' contains sample data
data = pd.read_csv('data.csv')

# Perform data analysis (e.g., calculate mean, median)
mean_value = data['value'].mean()
median_value = data['value'].median()

# Visualize data
data['value'].plot(kind='hist', bins=20, title='Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

print(f"Mean Value: {mean_value}")
print(f"Median Value: {median_value}")
