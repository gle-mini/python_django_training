import unittest
from unittest.mock import mock_open, patch
from io import StringIO
import sys
from numbers import read_and_print_numbers

class TestReadAndPrintNumbers(unittest.TestCase):
    def test_read_and_print_numbers(self):
        # Mock the open function to simulate file reading
        m = mock_open(read_data="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100")
        with patch('builtins.open', m):
            # Capture the output
            captured_output = StringIO()
            sys.stdout = captured_output

            # Call the function
            read_and_print_numbers()

            # Reset stdout
            sys.stdout = sys.__stdout__

            # Define expected output
            expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n"
            # Check if the captured output is as expected
            self.assertEqual(captured_output.getvalue(), expected_output)
        
    def test_file_not_found_exception(self):
        # Test FileNotFoundError exception handling
        with patch('builtins.open', side_effect=FileNotFoundError):
            # Capture the output
            captured_output = StringIO()
            sys.stdout = captured_output

            # Call the function
            read_and_print_numbers()

            # Reset stdout
            sys.stdout = sys.__stdout__

            # Check if the error message is correct
            self.assertIn("Error: The file 'numbers.txt' does not exist.", captured_output.getvalue())

    def test_general_exception(self):
        # Test general exception handling
        with patch('builtins.open', side_effect=Exception("Unexpected error")):
            # Capture the output
            captured_output = StringIO()
            sys.stdout = captured_output

            # Call the function
            read_and_print_numbers()

            # Reset stdout
            sys.stdout = sys.__stdout__

            # Check if the error message is correct
            self.assertIn("An error occurred: Unexpected error", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main(verbosity=2)
