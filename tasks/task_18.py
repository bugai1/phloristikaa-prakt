import unittest
from unittest.mock import patch, Mock
import requests

def send_request():
    return requests.post("https://api.example.com/v1/chat/completions", json={}, timeout=10)

class RequestTests(unittest.TestCase):
    @patch("requests.post")
    def test_success(self, post):
        post.return_value = Mock(status_code=200)
        self.assertEqual(send_request().status_code, 200)

    @patch("requests.post", side_effect=requests.Timeout)
    def test_timeout(self, post):
        with self.assertRaises(requests.Timeout):
            send_request()

if __name__ == "__main__":
    unittest.main()
