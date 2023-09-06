import json
import random

# Generate random data for 10 entries
data = []
for _ in range(10):
    entry = {
        "name": "Name" + str(_),
        "accountNumber": str(random.randint(1000000000, 9999999999)),
        "age": random.randint(18, 80)
    }
    data.append(entry)

# Save the data to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file 'data.json' has been generated.")
