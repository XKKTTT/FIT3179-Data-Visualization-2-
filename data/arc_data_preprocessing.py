import csv
import json
import os

# Get the current working directory
# new_directory = "/data"  # Replace with the path of your directory
os.chdir("/Users/mac/Desktop/FIT3179 Data Visualization 2/data")
current_directory = os.getcwd()

print("Current Directory:", current_directory)

# Open and read the CSV file
csv_file_path = "/asean_travel.csv"  # Replace this with your file path
json_file_path = "asean_travel.json"

# Initialize data structures
nodes = []
links = []
node_names = {}

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')  # adjust delimiter if needed
    header = next(csvreader)  # Skip the header row

    node_index = 0
    # Iterate through each row in the CSV
    for row in csvreader:
        dest_country = row[0].strip()
        orig_country = row[1].strip()

        # Add countries to the nodes list if not already present
        if dest_country not in node_names:
            nodes.append({"name": dest_country, "group": 1, "index": node_index})
            node_names[dest_country] = node_index
            node_index += 1
        
        if orig_country not in node_names:
            nodes.append({"name": orig_country, "group": 1, "index": node_index})
            node_names[orig_country] = node_index
            node_index += 1

        # Create links for each year
        years = [2020, 2021, 2022, 2023]
        for i, year in enumerate(years, start=2):  # 2020 starts at index 2
            value = int(row[i].replace(" ", "")) if row[i] else 0
            links.append({
                "source": node_names[orig_country],
                "target": node_names[dest_country],
                "value": value,
                "year": year
            })

# Create final dictionary structure
output_data = {
    "nodes": nodes,
    "links": links
}

# Write the output to a JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump(output_data, jsonfile, indent=4)

print(f"Data has been converted to JSON and saved as {json_file_path}")
