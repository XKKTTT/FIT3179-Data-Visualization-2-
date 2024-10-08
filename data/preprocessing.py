import pandas as pd
import os 

# print(os.getcwd())
print(os.getcwd())
os.chdir('./data')

print(os.getcwd())

import pandas as pd

# Load the dataset
df = pd.read_csv('arrivals_data.csv')

# Convert the 'date' column to datetime to extract the year
df['date'] = pd.to_datetime(df['date'])

# Extract the year from the 'date' column
df['year'] = df['date'].dt.year

# Group by 'soe' (state of entry) and 'year', summing up the number of arrivals
grouped_df = df.groupby(['soe', 'year'])['arrivals'].sum().reset_index()

# Save the new DataFrame to a CSV file
grouped_df.to_csv('soe_arrivals_by_year', index=False)

# Print a preview of the new DataFrame
print(grouped_df.head())
