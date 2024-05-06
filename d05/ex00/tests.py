from django.test import TestCase, Client
from django.http import HttpResponse
from unittest.mock import patch, Mock
import psycopg2

class InitViewTests(TestCase):
    def setUp(self):
        # The client will be used to make requests to your application
        self.client = Client()

    @patch('psycopg2.connect')
    def test_init_view_success(self, mock_connect):
        # Mock the connection and cursor
        mock_conn = mock_connect.return_value.__enter__.return_value
        mock_cursor = mock_conn.cursor.return_value.__enter__.return_value
        
        # Simulate a successful execution of the SQL command
        mock_cursor.execute.return_value = None
        mock_conn.commit.return_value = None
        
        response = self.client.get('/ex00/init/')  # Corrected URL
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "OK")

    @patch('psycopg2.connect')
    def test_init_view_failure(self, mock_connect):
        # Simulate a connection error
        mock_connect.side_effect = psycopg2.OperationalError("Cannot connect to database")
        
        response = self.client.get('/ex00/init/')  # Corrected URL
        print(f"Response Code: {response.status_code}")
        print(f"Response: {response.content.decode()}")
        self.assertNotEqual(response.status_code, 200)
        self.assertIn("An error occurred", response.content.decode())
