def extract_content(api_data):
    if not isinstance(api_data, dict):
        raise ValueError("Ответ должен быть объектом")
    choices = api_data.get("choices")
    if not isinstance(choices, list) or not choices:
        raise ValueError("choices отсутствует или пуст")
    if not isinstance(choices[0], dict):
        raise ValueError("Первый choice должен быть объектом")
    message = choices[0].get("message")
    if not isinstance(message, dict):
        raise ValueError("message отсутствует")
    content = message.get("content")
    if content is None:
        raise ValueError("content равен None")
    if not isinstance(content, str):
        raise ValueError("content должен быть строкой")
    if not content.strip():
        raise ValueError("content пуст")
    return content

examples = [
    {"choices": [{"message": {"content": "Готово"}}]},
    {"choices": []},
    {"choices": [{"role": "assistant"}]},
    {"choices": [{"message": {"content": ""}}]}
]
for item in examples:
    try:
        print(extract_content(item))
    except ValueError as error:
        print(error)
