configuration_1 = {
        'red': 12,
        'green': 13,
        'blue': 14
}

def get_empty_totals():
      return { 'red': 0, 'green': 0, 'blue': 0 }

def get_color_and_quantity(selection):
      selection = selection.strip().split(' ')
      quantity = int(selection[0])
      color = selection[1]
      return color, quantity

def is_game_valid(game):
     maxes = configuration_1
     rounds = game.split(';')
     for round in rounds:
          totals = get_empty_totals()
          draws = round.split(',')
          for selection in draws:
               color, quantity = get_color_and_quantity(selection)
               totals[color] += quantity
               if totals[color] > maxes[color]:
                    return False
     return True

def get_game_power(game):
    total = 1
    maxes = get_empty_totals()
    rounds = game.split(';')
    for round in rounds:
         totals = get_empty_totals()
         draws = round.split(',')
         for selection in draws:
              color, quantity = get_color_and_quantity(selection)
              totals[color] += quantity
              maxes[color] = max(maxes[color], totals[color])
    
    for color in maxes.keys():
        total *= maxes[color]
    return maxes, total

def get_game_and_number(game):
    split_1 = game.split(':')
    game_num = int(split_1[0].split(' ')[1])
    return split_1[1], game_num

def part_one(input):
  valid_game_ids = []
  for line in input:
     game, num = get_game_and_number(line)
     if is_game_valid(game):
        valid_game_ids.append(num)
  return sum(valid_game_ids)

def part_two(input):
  result = 0
  for line in input:
     game, _ = get_game_and_number(line)
     _, power= get_game_power(game)  
     result += power
  return result

if __name__ == '__main__':
  with open('input.txt', 'r') as f:
          lines = f.readlines()
          input = [line.strip() for line in lines]

  print('part 1', part_one(input))
  print('part 2:', part_two(input))
