import unittest
from part1 import *

class Test1(unittest.TestCase):
    def test_dissect_compartments(self):
        input = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        first_compartment, second_compartment = dissect_compartments(input)
        self.assertEqual('vJrwpWtwJgWr', first_compartment)
        self.assertEqual('hcsFMMfFFhFp', second_compartment)

    def test_find_similarities(self):
        first_compartment, second_compartment = 'vJrwpWtwJgWr', 'hcsFMMfFFhFp'
        result = find_similarities(first_compartment, second_compartment)
        self.assertEqual('p', result)

    def test_find_similarities_2(self):
        first_compartment, second_compartment = dissect_compartments('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')
        result = find_similarities(first_compartment, second_compartment)
        self.assertEqual('v', result)

    def test_rank_priority_lowercase(self):
        rank = rank_priority('p')
        self.assertEqual(16, rank)
    
    def test_rank_priority_uppercase(self):
        rank = rank_priority('P')
        self.assertEqual(42, rank)

    def test_process_rucksack(self):
        input = """
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw"""

        result = process_rucksack(input)
        self.assertEqual(157, result)

if __name__ == '__main__':
    unittest.main()