import unittest
from app import create_app, db
from flask import current_app
import json
import sys


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app().app.test_client()

    def test_hello_world(self):
        response = self.app.get('/status')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {"message": "ok"}
        )


if __name__ == '__main__':
    unittest.main()
