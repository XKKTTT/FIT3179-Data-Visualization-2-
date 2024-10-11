import pandas as pd
import os 
# Load your dataset
os.chdir('data')
df = pd.read_csv('arrivals_data.csv')

# Convert 'date' to datetime to extract the year
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Melt the dataset to have 'gender' and 'visitor_count' in separate columns
df_melted = pd.melt(df, id_vars=['year', 'soe'], value_vars=['arrivals_male', 'arrivals_female'],
                    var_name='gender', value_name='visitor_count')

# Replace 'arrivals_male' with 'Male' and 'arrivals_female' with 'Female'
df_melted['gender'] = df_melted['gender'].replace({'arrivals_male': 'Male', 'arrivals_female': 'Female'})

# Group by year, state, and gender, and calculate the total sum of arrivals
grouped_df = df_melted.groupby(['year', 'soe', 'gender']).agg({
    'visitor_count': 'sum'
}).reset_index()

# Print the result or save it to a new CSV
print(grouped_df)

# Save to a new file if needed
grouped_df.to_csv('grouped_visitors_by_year_state_gender.csv', index=False)