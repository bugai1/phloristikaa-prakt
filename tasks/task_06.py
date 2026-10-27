import json
headers = {"Authorization": "Bearer <API_KEY>", "Content-Type": "application/json"}
payload = {"model": "example-model", "messages": [{"role": "system", "content": "Верни JSON."}, {"role": "user", "content": "Привет"}]}
print(json.dumps(payload, ensure_ascii=False, indent=2))
