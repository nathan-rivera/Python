import json
import os
import random 
import random, string
import string
import pandas as pd

data ={  
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

directory = "C:\Temp"
num_files = 25

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the data to multiple JSON files
for i in range(num_files):
    filename = f"file{i + 1}.json"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

    print(f"File '{filename}' saved successfully.")
