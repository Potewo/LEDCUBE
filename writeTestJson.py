import json
d = {"a": "A", "b": "B"}
with open('writetest.json', 'w') as f:
    json.dump(d, f, indent=4)
