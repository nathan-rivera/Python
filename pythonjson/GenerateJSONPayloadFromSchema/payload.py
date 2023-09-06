import json 
import random 
import random, string
import string
import pandas as pd
N = 5
res = ''.join(random.choices(string.ascii_letters +
                             string.digits, k=N))
# python objects can store in json format  
value ={  
    "newAccount1": {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    
    "newAccount2": {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount3": {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount4" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount5" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount6" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount7" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount8" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount9" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount10" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount11" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
    },
    "newAccount12" + str(res): {  
        "name": "Ethan " + str(res) ,  
        "subject": "accountMember",  
        "age": (random.randint(18,50)),  
        "accountNumber": (random.randint(999,9999))
        },
    
}  
# the json file to saves the output data   
save_file = open("saveHIGdata.json", "w")  
json.dump(value, save_file, indent = 6)  
save_file.close()  
def writeToJSONFile(path, fileName, data):
    filePathNameWExt =  path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        json.dump(data, fp)
        fp.write(data)

writeToJSONFile("C:\Temp", "payloadPython", "payloadData")
# df = pd.read_json('data.json')
#
# print(df.to_string())
