from part1 import *

def get_result(input):
    if input == "X":
        return -1
    if input == "Y":
        return 0
    if input == "Z":
        return 1

def resolve_player_value(opponent, match_result):
    if match_result == 0:
        return opponent
    if opponent == "scissors":
        if match_result == 1:
            return "rock"
        else:
            return "paper"
    if opponent == "rock":
        if match_result == 1:
            return "paper"
        else:
            return "scissors"
    if opponent == "paper":
        if match_result == 1:
            return "scissors"
        else:
            return "rock"

def game_two(input):
    input = input.split('\n')

    sum = 0
    for i in range(0, len(input)):
        if input[i] == '':
            continue
        temp = input[i].split(' ')
        left, right = temp[0], temp[1]
        opponent, match_result = get_shape(left), get_result(right)
        player = resolve_player_value(opponent, match_result)
        player_value = get_shape_value(player)
        match_value = get_match_value(match_result)
        sum += (player_value + match_value)
    
    return sum

if __name__ == '__main__':
    f = open("input.txt", "r")
    output = f.read()
    result = game_two(output)
    print(result)
