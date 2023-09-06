import json
import random 
import random, string
import string
import pandas as pd

# the json file to saves the output data   

# save_file = open("C:\Temp\data.json", "a")
# json.dump('name:' 'Joe', save_file, indent = 4)  
# save_file.close()  
# df = pd.read_json('C:\Temp\data.json')
# print(df.to_string())


with open('C:\Temp\data.json', 'r') as f: 
    json_data = json.load(f)
    json_data['John Smith'] = "Jones"

with open('C:\Temp\data.json', 'w') as f:
    f.write(json.dumps(json_data))
    
    ##


# data['age'] = 31

# modified_json_string = json.dumps(data)
# print(modified_json_string)







# # Step 1: Read the JSON file
# with open("C:\Temp\data.json") as file:data = json.load(file)
# data['age'] = '55'
# with open("C:\Temp\data.json") as file:json.dump(data, file, indent=4)
