import unittest
from my_sort import sort_and_display_musicians

class TestMusicianSort(unittest.TestCase):
    def test_sort_and_display_musicians(self):
        from io import StringIO
        import sys
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        test_musicians = {
            'Hendrix': '1942',
            'Allman': '1946',
            'King': '1925',
            'Clapton': '1945',
            'Johnson': '1911',
            'Berry': '1926',
            'Vaughan': '1954',
            'Cooder': '1947',
            'Page': '1944',
            'Richards': '1943',
            'Hammett': '1962',
            'Cobain': '1967',
            'Garcia': '1942',
            'Beck': '1944',
            'Santana': '1947',
            'Ramone': '1948',
            'White': '1975',
            'Frusciante': '1970',
            'Thompson': '1949',
            'Burton': '1939'
        }
        
        expected_output = '''Johnson
King
Berry
Burton
Garcia
Hendrix
Richards
Beck
Page
Clapton
Allman
Cooder
Santana
Ramone
Thompson
Vaughan
Hammett
Cobain
Frusciante
White
'''
        sort_and_display_musicians(test_musicians)
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

