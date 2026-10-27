def extract_content(data):
    try:
        choices = data["choices"]
        if not isinstance(choices, list) or not choices:
            raise ValueError("choices пуст или имеет неверный тип")
        message = choices[0]["message"]
        if not isinstance(message, dict):
            raise ValueError("message должен быть объектом")
        content = message["content"]
        if not isinstance(content, str):
            raise ValueError("content должен быть строкой")
        return content
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("Неправильная структура ответа") from exc

print(extract_content({"choices": [{"message": {"content": "Привет!"}}]}))
