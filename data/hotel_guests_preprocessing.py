import pandas as pd
import csv
import json
import os

# Get the current working directory
# new_directory = "/data"  # Replace with the path of your directory
# current_directory = os.getcwd()
# print(os.listdir())
os.chdir("data")

# print("Current Directory:", current_directory)
# Assuming the data is in a CSV format
data = pd.read_csv('hotel_guests.csv')
print(data.head())
print(data.columns)
# Reshape the data from wide to long format
reshaped_data = data.melt(id_vars=["YEAR"], 
                          var_name="STATE", 
                          value_name="ARRIVALS")

# # Save the reshaped data to a new CSV
reshaped_data.to_csv('hotel_guests_wide', index=False)
