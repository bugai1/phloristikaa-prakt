import json
raw = '{"choices": [{"message": {"role": "assistant", "content": "Привет!"}}]}'
data = json.loads(raw)
print(len(data["choices"]))
print(data["choices"][0]["message"]["role"])
