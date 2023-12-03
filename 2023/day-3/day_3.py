special_characters = "!@#$%^&*()-+?_=,<>/"

def get_part_nums_from_line(candidates, grid, current_row_num):
  part_nums = []
  for candidate in candidates:
    num, start, end = candidate
    col_search_start = max(start - 1, 0)
    col_search_end = min(end + 2, len(grid[0]))

    # print('num', num, 'start', start, 'end', end, 'current_row_num', current_row_num)
    # print('col_search_start', col_search_start, 'col_search_end', col_search_end)

    if current_row_num > 0:
      for col in range(col_search_start, col_search_end):
        if grid[current_row_num - 1][col] in special_characters:
          part_nums.append([num, current_row_num, start, end])
          break
    
    if current_row_num < len(grid) - 1:
      for col in range(col_search_start, col_search_end):
        if grid[current_row_num + 1][col] in special_characters:
          part_nums.append([num, current_row_num, start, end])
          break

    for col in range(col_search_start, col_search_end):
      if grid[current_row_num][col] in special_characters:
        part_nums.append([num, current_row_num, start, end])
        break
    
  return part_nums

def find_gears(grid):
  gears = []
  for row_num, row in enumerate(grid):
    for col_num, col in enumerate(row):
      if col == '*':
        gears.append([row_num, col_num])
  return gears

def get_gear_ratio(gear, parts):
  gear_row, gear_col = gear

  eligible_parts = []

  for part in parts:
    num, part_row, part_start, part_end = part

    # if (num == 598):
    #   print('num', num)
    #   print('part_row', part_row, 'part_start', part_start, 'part_end', part_end)
    #   print('gear_row', gear_row, 'gear_col', gear_col)

    if part_row == gear_row:
      if part_start == gear_col + 1:
        eligible_parts.append(num)
      elif part_end == gear_col - 1:
        eligible_parts.append(num)

    if part_row == gear_row - 1 or part_row == gear_row + 1:
      if gear_col in range(part_start - 1, part_end + 2):
        eligible_parts.append(num)

  if len(eligible_parts) == 2:
    return (eligible_parts[0] * eligible_parts[1])
  
  return 0

def get_numeric_values_from_line(line):
  vals = []
  res = 0
  index = 100000
  for idx, i in enumerate(line):
    if i.isnumeric():
      index = min(index, idx)
      res = res * 10 + int(i)
    
    if idx + 1 == len(line):
      if res > 0:
        vals.append([res, index, idx])
    elif line[idx + 1].isnumeric() == False:
      if res > 0:
        vals.append([res, index, idx])
      res = 0
      index = 100000
    
  return vals

def part_one(input):
  result = []
  for idx, line in enumerate(input):
    candidates = get_numeric_values_from_line(line)
    part_nums = get_part_nums_from_line(candidates, input, idx)
    
    for part_num in part_nums:
      num, _, _, _ = part_num
      result.append(num)
  return sum(result)

def part_two(input):
  result = 0
  part_nums = []
  gears = find_gears(input)
  
  for idx, line in enumerate(input):
    candidates = get_numeric_values_from_line(line)
    line_part_nums = get_part_nums_from_line(candidates, input, idx)
    
    for part in line_part_nums:
      part_nums.append(part)

  for gear in gears:
    result += get_gear_ratio(gear, part_nums)
  return result

if __name__ == '__main__':
  with open('input.txt', 'r') as f:
          lines = f.readlines()
          input = [line.strip() for line in lines]

  print('part 1', part_one(input))
  print('part 2:', part_two(input))
