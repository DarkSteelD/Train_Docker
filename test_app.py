import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_data_endpoint(self):
        result = self.app.get('/data')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
