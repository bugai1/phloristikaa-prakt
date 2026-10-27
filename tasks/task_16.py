import json
def validate(data):
    required = {"category", "priority", "summary", "tags", "requires_human"}
    if required - set(data):
        raise ValueError("Не хватает обязательных полей")
    if data["category"] not in {"billing", "bug", "account", "feature_request", "other"}:
        raise ValueError("Недопустимая category")
    if data["priority"] not in {"low", "medium", "high"}:
        raise ValueError("Недопустимый priority")
    if not isinstance(data["summary"], str) or not data["summary"].strip():
        raise ValueError("Недопустимый summary")
    if not isinstance(data["tags"], list) or any(not isinstance(tag, str) for tag in data["tags"]):
        raise ValueError("Недопустимые tags")
    if type(data["requires_human"]) is not bool:
        raise ValueError("Недопустимый requires_human")
    return True

def build_payload(text, model):
    return {"model": model, "messages": [{"role": "system", "content": "Верни JSON классификации."}, {"role": "user", "content": text}]}

def extract_content(data):
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("Неправильная структура API") from exc
    if not isinstance(content, str):
        raise ValueError("content должен быть строкой")
    return content

def classify_fixture(text):
    payload = build_payload(text, "mock-model")
    raw = '{"category":"billing","priority":"high","summary":"Повторное списание","tags":["payment"],"requires_human":true}'
    result = json.loads(extract_content({"choices": [{"message": {"content": raw}}]}))
    validate(result)
    return payload, result

print(classify_fixture("Списали оплату")[1])
