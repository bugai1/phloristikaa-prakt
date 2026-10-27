def build_chat_url(base_url):
    base_url = base_url.strip()
    if not base_url or not base_url.startswith("https://"):
        raise ValueError("Нужен непустой HTTPS URL")
    return base_url.rstrip("/") + "/chat/completions"

print(build_chat_url("https://api.example.com/v1"))
print(build_chat_url("https://api.example.com/v1/"))
