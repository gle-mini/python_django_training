import unittest
from state import find_state_by_capital_city

class TestStateByCapital(unittest.TestCase):

    def test_known_capitals(self):
        """Test the function with capitals that are known to ensure it returns the correct state."""
        self.assertEqual(find_state_by_capital_city("Salem"), "Oregon")
        self.assertEqual(find_state_by_capital_city("Montgomery"), "Alabama")
        self.assertEqual(find_state_by_capital_city("Trenton"), "New Jersey")
        self.assertEqual(find_state_by_capital_city("Denver"), "Colorado")

    def test_unknown_capital(self):
        """Test the function with a capital city that is not in the dictionary to check proper handling."""
        self.assertEqual(find_state_by_capital_city("Paris"), "Unknown capital city")
        self.assertEqual(find_state_by_capital_city("London"), "Unknown capital city")

    def test_case_sensitivity(self):
        """Test the function with different case inputs to check for case sensitivity issues."""
        self.assertEqual(find_state_by_capital_city("salem"), "Unknown capital city")
        self.assertEqual(find_state_by_capital_city("DENVER"), "Unknown capital city")

    def test_empty_input(self):
        """Test the function with an empty string to see how it handles no input."""
        self.assertEqual(find_state_by_capital_city(""), "Unknown capital city")

if __name__ == "__main__":
    unittest.main()

