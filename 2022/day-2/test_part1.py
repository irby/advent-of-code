import unittest
from part1 import *

class Test1(unittest.TestCase):

    def test_get_shape(self):
        input = [["A","X"], ["B","Y"], ["C","Z"]]
        expected_result = ["rock", "paper", "scissors"]
        
        for i in range(0, len(input)):
            for j in range(0, len(input[i])):
                result = get_shape(input[i][j])
                self.assertEqual(result, expected_result[i])
            
    def test_get_winner(self):
        input = [["rock", "paper"], ["rock", "scissors"], ["rock", "rock"], ["scissors", "paper"], ["scissors", "rock"], ["scissors", "scissors"], ["paper", "rock"], ["paper", "scissors"], ["scissors", "scissors"]]
        expected_result = [1, -1, 0, -1, 1, 0, -1, 1, 0]
        for i in range(0, len(input)):
            result = get_winner(input[i][0], input[i][1])
            self.assertEqual(result, expected_result[i])

    def test_game(self):
        input = """A Y\nB X\nC Z"""
        result = game(input)
        self.assertEqual(result, 15)
    
if __name__ == '__main__':
    unittest.main()
