import json

data = [
    {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'},
]

with open('people.json', 'w') as file:
    json.dump(data, file)
