import os
import json

directory_path = 'C:\Temp\Output'
target_parameter = 'data1' 

# Iterate through all JSON files in the specified directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)

        # Load the existing JSON data
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        # Check if the target parameter exists in the JSON data
        if target_parameter in existing_data:
            # Update the data for the target parameter
            existing_data[target_parameter] = 'data99'

            # Write the updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
