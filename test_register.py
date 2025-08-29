# test_register.py
import sys
import os
sys.path.insert(0, os.path.abspath("backend"))

import unittest
import json
from backend.app import app  

class RegisterAPITestCase(unittest.TestCase):
    def setUp(self):
        # Enable testing mode
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_register_success(self):
        # Valid registration
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "secure123",
            "confirm_password": "secure123"
        }
        response = self.client.post(
            "/api/register",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(data["message"], "Account created successfully")
        self.assertIn("user_id", data["data"])

    def test_register_missing_field(self):
        # Missing email
        payload = {
            "username": "testuser",
            "password": "secure123",
            "confirm_password": "secure123"
        }
        response = self.client.post(
            "/api/register",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "All fields are required")

    def test_register_password_mismatch(self):
        payload = {
            "username": "testuser",
            "email": "testuser2@example.com",
            "password": "secure123",
            "confirm_password": "wrongpass"
        }
        response = self.client.post(
            "/api/register",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Passwords do not match")

    def test_register_short_password(self):
        payload = {
            "username": "testuser",
            "email": "testuser3@example.com",
            "password": "123",
            "confirm_password": "123"
        }
        response = self.client.post(
            "/api/register",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Password must be at least 6 characters long")


if __name__ == "__main__":
    unittest.main()
