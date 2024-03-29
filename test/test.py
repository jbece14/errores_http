import unittest
import json
from unittest.mock import MagicMock, patch
from flask import Flask, jsonify
from datetime import datetime, timezone, timedelta
from app.errores_http import *

class TestClass(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_success(self):
        with self.app.test_request_context('/'):
            response = success()
        self.assertEqual(response[1], 200)
    
    def test_created(self):
        with self.app.test_request_context('/'):
            response = created()
        self.assertEqual(response[1], 201)
    
    def test_bad_request_error_message(self):
        with self.app.test_request_context('/'):
            response = bad_request_error("test error")
        self.assertEqual(response[1], 400)

    def test_unauthorized_error_message(self):
        with self.app.test_request_context('/'):
            response = unauthorized_error("test error")
        self.assertEqual(response[1], 401)

    def test_forbidden_error_without_message(self):
        with self.app.test_request_context('/'):
            response = forbidden_error("test error")
        self.assertEqual(response[1], 403)
    
    def test_not_found_error_message(self):
        with self.app.test_request_context('/'):
            response = not_found_error("test error")
        self.assertEqual(response[1], 404)

    def test_not_allowed_error_message(self):
        with self.app.test_request_context('/'):
            response = not_allowed_error("test error")
        self.assertEqual(response[1], 405)

    def test_request_timeout_message(self):
        with self.app.test_request_context('/'):
            response = request_timeout("test error")
        self.assertEqual(response[1], 408)

    def test_too_many_request_message(self):
        with self.app.test_request_context('/'):
            response = too_many_request("test error")
        self.assertEqual(response[1], 429)

    def test_internal_server_error_message(self):
        with self.app.test_request_context('/'):
            response = internal_server_error("test error")
        self.assertEqual(response[1], 500)

    
    @patch("app.errores_http.datetime")
    def test_get_colombia_timestamp(self, mock_datetime):
        fixed_datetime = datetime(2022, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = fixed_datetime
        result = get_colombia_timestamp()
        expected_result = fixed_datetime.strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()