import pandas as pd 
import os
# Assuming the dataset is loaded into a DataFrame
# Replace 'your_file.csv' with the actual file name

os.chdir("data")

df = pd.read_csv('arrivals_data.csv')

# Convert 'date' to datetime to extract the year
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Group by 'year' and 'soe' (state) and sum the male and female arrivals
grouped_df = df.groupby(['year', 'soe']).agg({
    'arrivals_male': 'sum',
    'arrivals_female': 'sum'
}).reset_index()

# Print the result or save it to a new CSV
print(grouped_df)

# Save to a new file if needed
grouped_df.to_csv('grouped_visitors_by_year_state.csv', index=False)
