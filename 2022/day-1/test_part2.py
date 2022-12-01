import unittest
from part2 import *

class Test1(unittest.TestCase):

    def test_find_top_3(self):
        input = [100, 200, 500, 800, 1100, 300, 700, 900]
        result = find_top_3(input)
        self.assertEqual([1100, 900, 800], result)
    
if __name__ == '__main__':
    unittest.main()
