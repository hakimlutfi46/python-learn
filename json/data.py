import json

data = '{"Name": "Hakim", "Age": 20, "Hobby": "Mancing"}'

json_data = json.loads(data)

print(type(json_data))
print(json_data['Name'])
print(json_data['Age'])
print(json_data['Hobby'])