import json
import os

# Define the data for the JSON files
data_1 = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

data_2 = {
    "name": "Jane Smith",
    "age": 25,
    "city": "San Francisco"
}

# Specify the local directory to save the JSON files
directory = "C:\Temp"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create multiple JSON files
for i, data in enumerate([data_1, data_2]):
    file_name = f"file{i+1}.json"
    file_path = os.path.join(directory, file_name)

    # Open the file in write mode and create the JSON file
    with open(file_path, "w") as file:
        # Write the data to the file in JSON format
        json.dump(data, file)

    print(f"Created JSON file: {file_path}")
