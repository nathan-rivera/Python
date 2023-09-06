import json
import os
import random
import string

# Function to generate a random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Path to the directory containing JSON files
directory_path = 'C:\Temp\Output'

# Name of the parent parameter you want to update
parent_parameter_name = 'data3'

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)

        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Update parameters within the specific parent parameter
        if parent_parameter_name in data:
            parent_parameter = data[parent_parameter_name]
            parent_parameter['name'] = generate_random_string(10)
         #   parent_parameter['another_nested_key'] = generate_random_string(8)

        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

print("JSON files updated with random data strings within the specific parent parameter.")
