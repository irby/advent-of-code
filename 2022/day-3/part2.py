from part1 import *

def process_rucksack_groups(input):
    input = input.split('\n')
    input = ["{}".format(element.lstrip().rstrip()) for element in input]

    print('input', input)

    result = 0
    for i in range(0, len(input), 3):
        item1 = input[i]
        item2 = input[i + 1]
        item3 = input[i + 2]

        print(i, item1, item2, item3)

        similarity = find_similarities(item1, item2)
        similarity = find_similarities(similarity, item3)
        print('similarity', similarity)
        rank = rank_priority(similarity)
        result += rank
    return result

if __name__ == '__main__':
    f = open("input.txt", "r")
    output = f.read()
    result = process_rucksack_groups(output)
    print(result)