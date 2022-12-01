import unittest
from part1 import *

class Test1(unittest.TestCase):

    def test_breakupCalories(self):
        input = """
        100
        200
        300

        500
        600

        700
        """
        result = breakupCalories(input)
        self.assertEqual(3, len(result))
        self.assertEqual([100, 200, 300], result[0])
        self.assertEqual([500, 600], result[1])
        self.assertEqual([700], result[2])

    def test_count_breakup(self):
        input = [[100, 200, 300], [500, 600], [700]]
        result = count_breakup(input)
        self.assertEqual(3, len(result))
        self.assertEqual(600, result[0])
        self.assertEqual(1100, result[1])
        self.assertEqual(700, result[2])

    def test_find_max(self):
        input = [600, 1100, 700]
        result = find_max(input)
        self.assertEqual(1100, result)
    
if __name__ == '__main__':
    unittest.main()
