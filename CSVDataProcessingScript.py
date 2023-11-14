# Process CSV data using pandas

import pandas as pd

# Read CSV data
data = pd.read_csv('data.csv')

# Display basic statistics
print("Basic Statistics:")
print(data.describe())

# Filter and display specific columns
selected_data = data[['Name', 'Age', 'City']]
print("\nSelected Data:")
print(selected_data)
