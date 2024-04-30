import unittest
from io import StringIO
import sys
from var import my_var  # Import the my_var function

class TestMyVar(unittest.TestCase):
    def test_my_var_output(self):
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        my_var()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Define expected output
        expected_output = """42 has a type <class 'int'>
42 has a type <class 'str'>
quarante-deux has a type <class 'str'>
42.0 has a type <class 'float'>
True has a type <class 'bool'>
[42] has a type <class 'list'>
{42: 42} has a type <class 'dict'>
(42,) has a type <class 'tuple'>
set() has a type <class 'set'>
"""
        # Check if the captured output is as expected
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    # Set verbosity level to 2 (default is 1), which means more detailed output
    unittest.main(verbosity=2)

