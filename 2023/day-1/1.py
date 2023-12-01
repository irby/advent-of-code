def get_numbers_from_edges(edges):
  numbers = []
  for i in edges:
    val = str(i[0]) + str(i[1])
    numbers.append(int(val))
  return numbers

def get_edges(numbers):
  edges = []
  for i in numbers:
     if len(i) == 1:
      edges.append([i[0], i[0]])
      continue
     edges.append([i[0], i[-1]])
  return edges
      
def read_numbers_1(input):
  numbers = []
  if input != '':
    for val in input:
       if val.isnumeric():
          numbers.append(int(val))
  return numbers

NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def read_numbers_2(input):
   first = None
   last = None
   current = ''

   for i in input:
      current += i

      if i.isnumeric():
         first = first if first is not None else int(i)
         last = int(i)
         continue
      
      for index, num in enumerate(NUMBERS):
         if num not in current:
            continue
         first = first if first is not None else index
         last = index
         current = current[-1]
         break
         
   return [first, last]

if __name__ == '__main__':
    is_test = False
    input1 = is_test and 'sample.txt' or 'input.txt'
    input2 = is_test and 'sample2.txt' or 'input.txt'
    
    with open(input1, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    numbers = list(map(read_numbers_1, lines))
    edges = get_edges(numbers)
    edge_nums = get_numbers_from_edges(edges)
    
    print('part 1', sum(edge_nums))


    with open(input2, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    edges = list(map(read_numbers_2, lines))
    edge_nums = get_numbers_from_edges(edges)
    
    print('part 2', sum(edge_nums))
