import unittest
from part1 import *

class Test4(unittest.TestCase):
    def test_get_range(self):
        input = '2-4'
        result = get_range(input)
        self.assertEqual([2,3,4], result)

    def test_get_range_2(self):
        input = '6-6'
        result = get_range(input)
        self.assertEqual([6], result)

    def test_get_pair_ranges(self):
        input = '2-4,6-8'
        left_result, right_result = get_pair_ranges(input)
        self.assertEqual([2,3,4], left_result)
        self.assertEqual([6,7,8], right_result)

    def test_process_assignments(self):
        input = """2-4,6-8
                   2-3,4-5
                   5-7,7-9
                   2-8,3-7
                   6-6,4-6
                   2-6,4-8"""
        result = process_assignments(input)
        self.assertEqual(2, result)


    # def test_find_similarities_2(self):
    #     first_compartment, second_compartment = dissect_compartments('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')
    #     result = find_similarities(first_compartment, second_compartment)
    #     self.assertEqual('v', result)

    # def test_rank_priority_lowercase(self):
    #     rank = rank_priority('p')
    #     self.assertEqual(16, rank)
    
    # def test_rank_priority_uppercase(self):
    #     rank = rank_priority('P')
    #     self.assertEqual(42, rank)

    # def test_process_rucksack(self):
    #     input = """
    #     vJrwpWtwJgWrhcsFMMfFFhFp
    #     jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    #     PmmdzqPrVvPwwTWBwg
    #     wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    #     ttgJtRGJQctTZtZT
    #     CrZsJsPPZsGzwwsLwLmpwMDw"""

    #     result = process_rucksack(input)
    #     self.assertEqual(157, result)

if __name__ == '__main__':
    unittest.main()