import unittest
from unittest.mock import patch
import os
import request_wikipedia

class TestWikipediaRequest(unittest.TestCase):
    def setUp(self):
        """ Set up for the tests """
        self.test_search_term = "Python"
        self.test_filename = "Python.wiki"

    def tearDown(self):
        """ Clean up after tests """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    @patch('request_wikipedia.requests.get')
    def test_fetch_wikipedia_content_valid(self, mock_get):
        """ Test fetching content with a valid search term """
        # Mocking the API responses
        mock_get.return_value.json.return_value = {
            'query': {
                'search': [{'pageid': 12345}],
                'pages': {
                    '12345': {
                        'extract': 'Python is a high-level programming language.'
                    }
                }
            }
        }

        content = request_wikipedia.fetch_wikipedia_content(self.test_search_term)
        self.assertIn('Python is a high-level programming language.', content)

    @patch('request_wikipedia.requests.get')
    def test_fetch_wikipedia_content_invalid(self, mock_get):
        """ Test fetching content with an invalid search term """
        mock_get.return_value.json.return_value = {'query': {'search': []}}
        content = request_wikipedia.fetch_wikipedia_content("xyzzyspoon!")
        self.assertIsNone(content)

    def test_write_to_file(self):
        """ Test that content is written to a file correctly """
        test_content = "Sample content"
        request_wikipedia.write_to_file(test_content, self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))
        with open(self.test_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        self.assertEqual(content, test_content)

    @patch('request_wikipedia.sys.argv', ['request_wikipedia.py'])
    def test_main_no_arguments(self):
        """ Test the main function with no arguments """
        with self.assertRaises(SystemExit) as cm:
            request_wikipedia.main()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()

