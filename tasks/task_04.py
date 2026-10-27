import json
samples = ['{"ok": true}', '{"ok": true,}', 'ответ модели: готово']
for raw in samples:
    try:
        print(json.loads(raw))
    except json.JSONDecodeError:
        print("Некорректный JSON")
