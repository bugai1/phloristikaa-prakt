problems = [
    "API-ключ записан прямо в коде.",
    "Нет Bearer перед ключом в Authorization.",
    "Нет timeout, поэтому запрос может зависнуть.",
    "Нет проверки HTTP-статуса.",
    "data=str(payload) не отправляет JSON корректным способом.",
    "Нет проверки структуры choices/message/content.",
    "Внутренний JSON content не разбирается отдельно.",
    "Нет проверки обязательных полей и типов.",
    "Печатаются response.headers, которые могут раскрывать чувствительные данные.",
    "Нет обработки сетевых, HTTP и JSON-ошибок."
]
for number, problem in enumerate(problems, 1):
    print(f"{number}. {problem}")
