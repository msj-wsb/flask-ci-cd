import unittest

from app import app

class FlaskTestCase(unittest.TestCase):

    def test_hello_world(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')
