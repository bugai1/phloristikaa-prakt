def check_required_fields(data):
    required = {"category", "priority", "summary", "tags", "requires_human"}
    missing = required - set(data)
    if missing:
        raise ValueError("Не хватает полей: " + ", ".join(sorted(missing)))
    return True

check_required_fields({"category": "bug", "priority": "high", "summary": "Сбой", "requires_human": True})
