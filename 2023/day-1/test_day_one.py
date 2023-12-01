import unittest
from day_one import *

with open('sample1.txt', 'r') as f:
        lines = f.readlines()
        sample_1 = [line.strip() for line in lines]

with open('sample2.txt', 'r') as f:
        lines = f.readlines()
        sample_2 = [line.strip() for line in lines]

class Test(unittest.TestCase):
        
        def test_partOne(self):
            result = solve_1(sample_1)
            self.assertEqual(142, result)
        
        def test_partTwo(self):
            result = solve_2(sample_2)
            self.assertEqual(281, result)

if __name__ == '__main__':
    unittest.main()
