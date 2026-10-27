def is_success(status_code):
    return 200 <= status_code <= 299

for code in [200, 401, 403, 404, 429, 500, 204]:
    print(code, "успех" if is_success(code) else "ошибка")
