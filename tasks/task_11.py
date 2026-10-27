import json
content = '{"category":"bug","priority":"high"}'
data = json.loads(content)
if not isinstance(data, dict):
    raise ValueError("Ожидался JSON-объект")
print(data)
