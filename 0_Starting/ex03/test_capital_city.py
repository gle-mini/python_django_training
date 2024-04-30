import unittest
from capital_city import find_capital_city

class TestCapitalCity(unittest.TestCase):

    def test_known_states(self):
        """Test known states to check if the function returns the correct capital city."""
        self.assertEqual(find_capital_city("Oregon"), "Salem")
        self.assertEqual(find_capital_city("Alabama"), "Montgomery")
        self.assertEqual(find_capital_city("New Jersey"), "Trenton")
        self.assertEqual(find_capital_city("Colorado"), "Denver")

    def test_unknown_state(self):
        """Test input with an unknown state to see if the function handles it correctly."""
        self.assertEqual(find_capital_city("Ile-De-France"), "Unknown state")
        self.assertEqual(find_capital_city("California"), "Unknown state")

    def test_case_sensitivity(self):
        """Test case sensitivity of the state names."""
        self.assertEqual(find_capital_city("oregon"), "Unknown state")
        self.assertEqual(find_capital_city("ALABAMA"), "Unknown state")

    def test_empty_input(self):
        """Test the function with an empty string as input."""
        self.assertEqual(find_capital_city(""), "Unknown state")

if __name__ == "__main__":
    unittest.main()

