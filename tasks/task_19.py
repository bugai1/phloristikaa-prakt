import json
import uuid
from pathlib import Path

def save_result(data, model="mock-model"):
    output = Path("output")
    output.mkdir(exist_ok=True, parents=True)
    result = {"request_id": str(uuid.uuid4()), "model": model, "status": "validated", **data}
    with (output / "result.json").open("w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)

save_result({"category": "bug", "priority": "low", "summary": "Ошибка", "tags": [], "requires_human": False})
