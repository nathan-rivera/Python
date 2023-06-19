import os
import json

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

# Create a list of directory paths to save the JSON files
directories = ["C:\Temp", "C:\Dell"]

for i, data in enumerate([data_1, data_2]):
    directory = directories[i]
    file_name = f"file{i+1}.json"
    file_path = os.path.join(directory, file_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Open the file in write mode and create the JSON file
    with open(file_path, "w") as file:
        # Write the data to the file in JSON format
        json.dump(data, file)

    print(f"Created JSON file: {file_path}")
