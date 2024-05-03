import unittest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
from geohashing import main

class TestGeoHashScript(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture prints for assertions
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_correct_arguments(self):
        test_args = ["python3 geohashing.py", "37.421542", "-122.085589", "2005-05-26-10458.68"]
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)

    def test_incorrect_argument_count(self):
        test_args = ["python3 geohashing.py", "37.421542", "-122.085589"]  # Missing datedow
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 1)
            self.assertIn('3 arguments required', self.held_stdout.getvalue())

    def test_invalid_latitude(self):
        test_args = ["python3 geohashing.py", "not_a_float", "-122.085589", "2005-05-26-10458.68"]
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 1)
            self.assertIn('Latitude and longitude must be valid numbers.', self.held_stdout.getvalue())

    def test_invalid_longitude(self):
        test_args = ["python3 geohashing.py", "37.421542", "not_a_float", "2005-05-26-10458.68"]
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 1)
            self.assertIn('Latitude and longitude must be valid numbers.', self.held_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

