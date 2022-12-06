import unittest
from part2 import *

class Test2(unittest.TestCase):
    def test_process_rucksack_groups(self):
        input = """vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw"""

        result = process_rucksack_groups(input)
        self.assertEqual(70, result)

if __name__ == '__main__':
    unittest.main()