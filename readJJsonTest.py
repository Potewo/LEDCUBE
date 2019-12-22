import json

with open("readtest.json", 'r') as f:
    json_data = json.load(f)

name_list = ["A", "B"]
for name in name_list:
    data = json_data[name]
    for i in data:
        for j in i:
            print(j)
