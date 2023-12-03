import unittest
from day_3 import *

with open('sample.txt', 'r') as f:
          lines = f.readlines()
          sample = [line.strip() for line in lines]

class Test(unittest.TestCase):
        
        def test_part_one(self):
            result = part_one(sample)
            self.assertEqual(4361, result)
        
        def test_part_two(self):
            result = part_two(sample)
            self.assertEqual(467835, result)

if __name__ == '__main__':
    unittest.main()
