import json
data = {"category": "обращение", "priority": "высокий", "tags": ["оплата", "ошибка"]}
print(json.dumps(data, ensure_ascii=False, indent=2))
print(repr(data))
