import unittest
from day6 import *

class Day6(unittest.TestCase):
    def test_find_marker(self):
        input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        result = find_marker(input)
        self.assertEqual(7, result)

    def test_find_marker_1(self):
        input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        result = find_marker(input)
        self.assertEqual(5, result)

    def test_find_marker_2(self):
        input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        result = find_marker(input)
        self.assertEqual(10, result)


    def test_find_marker_3(self):
        input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        result = find_marker_2(input)
        self.assertEqual(19, result)

    def test_find_marker_4(self):
        input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        result = find_marker_2(input)
        self.assertEqual(29, result)

if __name__ == '__main__':
    unittest.main()