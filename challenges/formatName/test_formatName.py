'''
Test formatName.py with unittest
Run tests:  python test_formatName.py 
'''

import unittest
from formatName import formatName 

class TestfName(unittest.TestCase):
    
    def test_single_name(self):
        '''
        One word names should be returned as one word names
        '''
        myName = "Prince"
        newName = formatName(myName)
        self.assertEqual(newName, "Prince")

    def test_multiple_middle_names(self):
        '''
        Testing names with multiple middle names shall be abbreviated
        '''
        myName = "Elizabeth Rosemond Hilton Wilding Todd Fisher Burton Warner Fortensky Taylor"
        newName = formatName(myName)
        self.assertEqual(newName, "Taylor, Elizabeth R. H. W. T. F. B. W. F.")
    
    def test_one_letter_middle_name(self):
        '''
        Testing names with one letter middle names shall not be abbreviated
        '''
        myName = "Bala X Krish"
        newName = formatName(myName)
        self.assertEqual(newName, "Krish, Bala X")

    def test_no_middle_name(self):
        '''
        Testing names with no middle names shall only return first and last name
        '''
        myName = "Thomas Narten"
        newName = formatName(myName)
        self.assertEqual(newName, "Narten, Thomas")

    def test_multiple_constaints(self):
        '''
        Testing names with one letter middle names and multiple middle names of different lengths
        '''
        myName = "Liz A Bo To Joe"
        newName = formatName(myName)
        self.assertEqual(newName, "Joe, Liz A B. T.")

    def test_one_middle_name(self):
        '''
        Testing names with one first, middle, and last name
        '''
        myName = "Barak Hussein Obama"
        newName = formatName(myName)
        self.assertEqual(newName, "Obama, Barak H.")

if __name__ == '__main__':
    unittest.main()