def get_shape(input):
    if input == 'A' or input == 'X':
        return 'rock'
    if input == 'B' or input == 'Y':
        return 'paper'
    if input == 'C' or input == 'Z':
        return 'scissors'
    raise ValueError()

def get_winner(opponent_value, player_value):
    if opponent_value == player_value:
        return 0
    if opponent_value == 'rock':
        if player_value == 'paper':
            return 1
        if player_value == 'scissors':
            return -1
    if opponent_value == 'scissors':
        if player_value == 'rock':
            return 1
        if player_value == 'paper':
            return -1
    if opponent_value == 'paper':
        if player_value == 'scissors':
            return 1
        if player_value == 'rock':
            return -1
    raise ValueError()

def get_shape_value(input):
    if input == "rock":
        return 1
    if input == "paper":
        return 2
    if input == "scissors":
        return 3
    raise ValueError()

def get_match_value(input):
    if input == -1:
        return 0
    if input == 0:
        return 3
    if input == 1:
        return 6
    raise ValueError()

def game(input):
    input = input.split('\n')

    sum = 0
    for i in range(0, len(input)):
        if input[i] == '':
            continue
        temp = input[i].split(' ')
        left, right = temp[0], temp[1]
        opponent, player = get_shape(left), get_shape(right)
        match = get_winner(opponent, player)
        match_value = get_match_value(match)
        player_shape_value = get_shape_value(player)
        print([left, right], [opponent, player], 'win?', match, 'match_value', match_value, 'player_value', player_shape_value)
        #print('player', player, 'opponent', opponent, 'win?', match, 'match value', match_value, 'player_value', player_shape_value)
        sum += (match_value + player_shape_value)
    
    return sum

    

if __name__ == '__main__':
    f = open("input.txt", "r")
    output = f.read()
    result = game(output)
    print(result)
