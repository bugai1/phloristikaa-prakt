import requests
import json

def describe_request_error(error):
    if isinstance(error, requests.Timeout):
        return "Тайм-аут: попробуйте позже."
    if isinstance(error, requests.HTTPError):
        return "HTTP-ошибка: проверьте статус ответа."
    if isinstance(error, requests.RequestException):
        return "Сетевая ошибка: проверьте соединение."
    if isinstance(error, json.JSONDecodeError):
        return "Внешний JSON имеет неверный формат."
    return "Ошибка формата данных."

