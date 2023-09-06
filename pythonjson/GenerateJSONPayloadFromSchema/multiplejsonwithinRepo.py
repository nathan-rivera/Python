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

# Create multiple JSON files
file_names = ["file1.json", "file2.json"]

for i, data in enumerate([data_1, data_2]):
    file_name = file_names[i]

    # Open the file in write mode and create the JSON file
    with open(file_name, "w") as file:
        # Write the data to the file in JSON format
        json.dump(data, file)

    print(f"Created JSON file: {file_name}")