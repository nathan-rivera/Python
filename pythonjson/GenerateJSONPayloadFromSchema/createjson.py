
import json 
import random 
import random, string
import string
import pandas as pd
# N = 5
# res = ''.join(random.choices(string.ascii_letters +
# # #                            string.digits, k=N))
value ={  
    "data1": {  
        "name": "John Smith",  
        "accountNumber": "1234567890",  
        "age": 25,  
        
    },
    
    "data2": {  
        "name": "Janet Smith",  
        "accountNumber": "0987654321",  
        "age": 30,  
        
    },
    "data3": {  
        "name": "Michael Johnson",  
        "accountNumber": "5678901234",  
        "age": 45,  
        
    },
    "data4" : {  
        "name": "Emily Davis",  
        "accountNumber": "4321098765",  
        "age": 35,  
        
    },
    "data5" : {  
        "name": "David Wilson",  
        "accountNumber": "9876543210",  
        "age": 50,  
    },
    "data6" : {  
        "name": "Olivia Thompson",  
        "accountNumber": "3456789012",  
        "age": 28,  
    },
    "data7" : {  
        "name": "Andrew Lee",
        "account_number": "2109876543",
        "age": 32  
    
    },
    "data8" : { 
        "name": "Sophia Miller",
        "account_number": "6789012345",
        "age": 41
    },
    "data9" : { 
        "name": "Daniel Anderson",
        "account_number": "5432109876",
        "age": 37
    },
    "data10" : { 
        "name": "Ava Martinez",
        "account_number": "9012345678",
        "age": 29
    },
    
        
    
}  
# the json file to saves the output data   
save_file = open("C:\Temp\data.json", "w")  
json.dump(value, save_file, indent = 6)  
save_file.close()  
df = pd.read_json('C:\Temp\data.json')
print(df.to_string())

######################################################
# # Load the JSON data
# data = json.loads(json_data)
# # Modify the data
# data["data"][0]["age"] = 26
# data["data"][1]["name"] = "Janet Smith"
# # Convert back to JSON string
# updated_json_data = json.dumps(data, indent=2)
# # Print the updated JSON data string
# print(updated_json_data)


# Parse the JSON data string into a Python dictionary
# data_dict = json.loads('data')
# # Update the values
# data_dict['data2'][0]['age'] = 26
# data_dict['data'][1]['name'] = 'Janet Smith'
# data_dict['data'][2]['accountNumber'] = '1111111111'
# # Convert the updated dictionary back to a JSON string
# updated_json_data = json.dumps(data_dict, indent=2)
# # Print the updated JSON data string
# print(updated_json_data)




# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt =  path + '/' + fileName + '.json'
#     with open(filePathNameWExt, 'a') as fp:
#         json.dump(data, fp)
#         fp.write(data)
# def writeToJSONFile("C:\Temp", "payloadPython", data):
#     with open("C:\Temp", 'a') as fp:
#         json.dump(data, fp)
#         fp.write(data)
        
        
# df = pd.read_json('data.json')
#
# print(df.to_string())
#
# filename = 'saveHIGdata.json'
# entry = {'carl': 33}
# # 1. Read file contents
# with open("C:\Temp\saveHIGdata.json", "r") as file:
#     data = json.load(file)
# # 2. Update json object
# data.append(entry)
# # 3. Write json file
# with open("C:\Temp\saveHIGdata.json", "w") as file:
#     json.dump(data, file)
# Sample JSON data string
