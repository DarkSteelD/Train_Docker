import unittest
from fastapi.testclient import TestClient
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_data_endpoint(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
