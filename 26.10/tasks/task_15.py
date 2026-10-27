CATEGORIES = {"billing", "bug", "account", "feature_request", "other"}
PRIORITIES = {"low", "medium", "high"}

def validate(data):
    required = {"category", "priority", "summary", "tags", "requires_human"}
    missing = required - set(data)
    if missing:
        raise ValueError("Не хватает полей: " + ", ".join(sorted(missing)))
    if not isinstance(data["category"], str) or data["category"] not in CATEGORIES:
        raise ValueError("Поле category недопустимо")
    if not isinstance(data["priority"], str) or data["priority"] not in PRIORITIES:
        raise ValueError("Поле priority недопустимо")
    if not isinstance(data["summary"], str) or not data["summary"].strip():
        raise ValueError("Поле summary должно быть непустой строкой")
    if not isinstance(data["tags"], list) or any(not isinstance(tag, str) for tag in data["tags"]):
        raise ValueError("Поле tags должно быть списком строк")
    if type(data["requires_human"]) is not bool:
        raise ValueError("Поле requires_human должно быть bool")
    return True
