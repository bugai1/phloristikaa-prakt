# phloristikaa prakt

Репозиторий для практических заданий. Текущая работа: `llm_ticket_triage`.

## Запуск текущего задания

Требуется Python 3.10 или новее.

```powershell
cd llm_ticket_triage
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py --mock
python -m unittest discover -s tests -v
```

Для запуска других заданий добавляйте отдельные папки в корень репозитория.
