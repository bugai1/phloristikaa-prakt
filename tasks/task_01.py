import json
raw = '{"name": "Mira", "age": 20}'
result = json.loads(raw)
print(result["name"])
print(result["age"])
print(type(result))
