import os
import json


directory_path = "C:\Temp\Output"  # Replace with the actual directory path

parent_parameter = "data3"

parameter_to_update = "name"

new_value = "Frank Pomarico"


# Iterate through all files in the directory

for filename in os.listdir(directory_path):

    if filename.endswith(".json"):

        file_path = os.path.join(directory_path, filename)


        # Open the JSON file for reading and writing

        with open(file_path, "r") as json_file:

            data = json.load(json_file)


        # Check if the parent parameter exists

        if parent_parameter in data and parameter_to_update in data[parent_parameter]:

            data[parent_parameter][parameter_to_update] = new_value


            # Write the updated data back to the JSON file

            with open(file_path, "w") as json_file:

                json.dump(data, json_file, indent=4)  
                # Optional: Use indent for pretty formatting