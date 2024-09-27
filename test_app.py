import unittest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch('app.get_db_connection')
    def test_data_endpoint(self, mock_get_db_connection):
        # Mock the async database connection
        async def mock_fetch(query):
            return [{'id': 1, 'name': 'Test'}]

        async def mock_close():
            pass

        mock_conn = AsyncMock()
        mock_conn.fetch = mock_fetch
        mock_conn.close = mock_close
        mock_get_db_connection.return_value = mock_conn

        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': 1, 'name': 'Test'}])

if __name__ == '__main__':
    unittest.main()
