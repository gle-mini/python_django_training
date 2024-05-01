import unittest
from all_in import analyze_inputs

class TestAllIn(unittest.TestCase):
    
    def test_correct_identifications(self):
        """Tests if correct identifications are made for states and capitals."""
        input_string = "Oregon, Denver, New Jersey, Montgomery"
        expected_results = [
            "Salem is the capital of Oregon",
            "Denver is the capital of Colorado",
            "Trenton is the capital of New Jersey",
            "Montgomery is the capital of Alabama"
        ]
        results = analyze_inputs(input_string)
        self.assertEqual(results, expected_results)

    def test_incorrect_identifications(self):
        """Tests handling of inputs that are neither states nor capitals."""
        input_string = "Silicon Valley, Gotham, ,"
        expected_results = [
            "Silicon Valley is neither a capital city nor a state",
            "Gotham is neither a capital city nor a state"
        ]
        results = analyze_inputs(input_string)
        self.assertEqual(results, expected_results)

    def test_case_sensitivity_and_spaces(self):
        """Tests that inputs are correctly identified regardless of case and extra spaces."""
        input_string = "  salem  , new jersey , oReGoN , DENVER  "
        expected_results = [
            "Salem is the capital of Oregon",
            "Trenton is the capital of New Jersey",
            "Salem is the capital of Oregon",
            "Denver is the capital of Colorado"
        ]
        results = analyze_inputs(input_string)
        self.assertEqual(results, expected_results)

    def test_empty_and_successive_commas(self):
        """Tests that no output is generated for empty input or successive commas."""
        input_string = " , , ,"
        results = analyze_inputs(input_string)
        self.assertIsNone(results)  # Expected None to indicate no processing should occur

if __name__ == "__main__":
    unittest.main()

