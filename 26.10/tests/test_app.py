import json
import tempfile
import unittest
import sys
from pathlib import Path
from unittest.mock import Mock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import requests

import app

VALID = {
    "category": "billing",
    "priority": "high",
    "summary": "Повторное списание",
    "tags": ["payment"],
    "requires_human": True
}

class AppTests(unittest.TestCase):
    def test_parse_model_json(self):
        self.assertEqual(app.parse_model_json(json.dumps(VALID)), VALID)

    def test_invalid_model_json(self):
        with self.assertRaises(app.AppError):
            app.parse_model_json("{bad json")

    def test_missing_field(self):
        data = dict(VALID)
        del data["tags"]
        with self.assertRaisesRegex(ValueError, "tags"):
            app.validate_result(data)

    def test_invalid_priority(self):
        data = dict(VALID)
        data["priority"] = "urgent"
        with self.assertRaisesRegex(ValueError, "priority"):
            app.validate_result(data)

    def test_bool_type(self):
        data = dict(VALID)
        data["requires_human"] = 1
        with self.assertRaisesRegex(ValueError, "requires_human"):
            app.validate_result(data)

    def test_extract_content(self):
        response = {"choices": [{"message": {"content": json.dumps(VALID)}}]}
        self.assertEqual(app.extract_content(response), json.dumps(VALID))

    def test_missing_choices(self):
        with self.assertRaises(app.AppError):
            app.extract_content({})

    def test_mock_result(self):
        self.assertEqual(app.mock_result("С меня дважды списали оплату")["category"], "billing")

    def test_save_result(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "output" / "result.json"
            app.save_result(VALID, path)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["status"], "validated")
            self.assertEqual(saved["category"], "billing")
            self.assertNotIn("api_key", saved)

    @patch("app.requests.post")
    def test_http_401(self, post):
        response = Mock()
        response.status_code = 401
        response.raise_for_status.side_effect = requests.HTTPError(response=response)
        post.return_value = response
        config = {"base_url": "https://api.example.com/v1", "api_key": "test", "model": "test"}
        with self.assertRaisesRegex(app.AppError, "401"):
            app.call_llm("test", config)

    @patch("app.requests.post", side_effect=requests.Timeout)
    def test_timeout(self, post):
        config = {"base_url": "https://api.example.com/v1", "api_key": "test", "model": "test"}
        with self.assertRaisesRegex(app.AppError, "ожидания"):
            app.call_llm("test", config)

if __name__ == "__main__":
    unittest.main()
