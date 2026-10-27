# AI Ticket Triage

CLI-приложение классифицирует обращение в поддержку и сохраняет проверенный JSON.

## Установка

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Mock-режим

```powershell
python app.py --mock "С меня дважды списали оплату за один заказ"
```

Если текст не передан аргументом, приложение запросит его через `input()`.

## Тесты

```powershell
python -m unittest discover -s tests -v
```

## Реальный API

Скопируйте `.env.example` в `.env` и укажите настройки совместимого Chat Completions API. Не добавляйте `.env` в Git.

```powershell
Copy-Item .env.example .env
python app.py --real "С меня дважды списали оплату за один заказ"
```

Успешный результат записывается в `output/result.json`. Папка `output` не добавляется в Git.
