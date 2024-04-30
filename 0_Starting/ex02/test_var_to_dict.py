import unittest
from var_to_dict import convert_list_to_dict

class TestVarToDict(unittest.TestCase):

    def test_convert_list_to_dict(self):
        # Call the function from var_to_dict.py
        result = convert_list_to_dict()

        # Expected results
        expected = {
            '1911': 'Johnson',
            '1925': 'King',
            '1926': 'Berry',
            '1939': 'Burton',
            '1942': 'Hendrix Garcia',
            '1943': 'Richards',
            '1944': 'Page Beck',
            '1945': 'Clapton',
            '1946': 'Allman',
            '1947': 'Cooder Santana',
            '1948': 'Ramone',
            '1949': 'Thompson',
            '1954': 'Vaughan',
            '1962': 'Hammett',
            '1967': 'Cobain',
            '1970': 'Frusciante',
            '1975': 'White'
        }

        # Check if the result matches the expected dictionary
        self.assertEqual(result, expected)
    

if __name__ == '__main__':
    unittest.main()
    
