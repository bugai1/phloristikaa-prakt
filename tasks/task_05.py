import os
from dotenv import load_dotenv
load_dotenv()
required = ["LLM_BASE_URL", "LLM_API_KEY", "LLM_MODEL"]
for name in required:
    if not os.getenv(name):
        print(f"Отсутствует настройка: {name}")
    else:
        print(f"{name}: задана")
