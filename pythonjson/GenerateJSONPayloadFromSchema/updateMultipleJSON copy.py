import os
import json
import shutil
import json
import random 
import random, string
import string
import pandas as pd


source_directory = "C:\Temp\Output"
destination_directory = "C:\Temp\Input"

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

for filename in os.listdir(source_directory):
    if filename.endswith(".json"):
        source_file_path = os.path.join(source_directory, filename)
        destination_file_path = os.path.join(destination_directory, filename)

        with open(source_file_path, "r") as source_file:
            data = json.load(source_file)
            
            # Update the JSON data as needed
            # For example, let's change the value of a key called "example_key"
            data["example_key"] = "new_value"

        with open(destination_file_path, "w") as destination_file:
            json.dump(data, destination_file, indent=4)

# Optional: Remove the source directory after updating and saving the files
shutil.rmtree(source_directory)