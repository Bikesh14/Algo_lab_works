import unittest
from search import binarySearch

class SearchTest(unittest.TestCase):
    def testbinary_search(self):   #function name must start with test
        values=[2,4,5,6,8,10,12]
        self.assertEqual(binarySearch(values, 6), 3)
        self.assertEqual(binarySearch(values, 2), 0)
        self.assertEqual(binarySearch(values, 10), 5)
        self.assertEqual(binarySearch(values, 20), 0)

if __name__=="__main__":
    unittest.main()
