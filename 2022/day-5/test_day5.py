import unittest
from day5 import DayFive

class Day5(unittest.TestCase):
    day5 = DayFive()
    def test_get_range(self):
        input = """
            [D]    
        [N] [C]    
        [Z] [M] [P]
         1   2   3 
        """
        result = self.day5.build_tower(input)
        self.assertEqual([['N','Z'], ['D','C','M'],['P']], result)

    def test_parse_instruction(self):
        instruction = 'move 1 from 2 to 3'
        num_items, from_index, to_index = self.day5.parse_instruction(instruction)
        self.assertEqual(1, num_items)
        self.assertEqual(2, from_index)
        self.assertEqual(3, to_index)

    def test_handle_instruction(self):
        tower = [['N','Z'], ['D','C','M'],['P']]
        num_items, from_index, to_index = 1, 2, 1
        result = self.day5.handle_instruction(tower, num_items, from_index, to_index)
        self.assertEqual([['D','N','Z'], ['C','M'],['P']], result)

    def test_e2e_part1(self):
        input = """
            [D]    
        [N] [C]    
        [Z] [M] [P]
         1   2   3 

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
        """
        result = self.day5.e2e_part1(input)
        self.assertEqual('CMZ', result)

    def test_e2e_part2(self):
        input = """
            [D]    
        [N] [C]    
        [Z] [M] [P]
         1   2   3 

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
        """
        result = self.day5.e2e_part2(input)
        self.assertEqual('MCD', result)

if __name__ == '__main__':
    unittest.main()