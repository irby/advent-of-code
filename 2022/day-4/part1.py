def get_range(section):
    range = [int(section[0:section.find("-")]), int(section[section.find("-")+1:])]
    return range

def get_pair_ranges(input):
    splits = input.split(',')
    left_range_section, right_range_section = splits[0], splits[1]
    left_range = get_range(left_range_section)
    right_range = get_range(right_range_section)
    return left_range, right_range

def is_overlap(left_range, right_range):
    left_min = left_range[0]
    left_max = left_range[-1]
    right_min = right_range[0]
    right_max = right_range[-1]
    return (left_min >= right_min and left_max <= right_max) or (left_min <= right_min and left_max >= right_max)

def is_overlap_2(left_range, right_range):
    left_min = left_range[0]
    left_max = left_range[-1]
    right_min = right_range[0]
    right_max = right_range[-1]
    return (left_min <= right_min <= left_max) or (left_min <= right_max <= left_max) or (right_min <= left_min <= right_max) or (right_min <= left_max <= right_max)

def parse_input(input):
    input = input.split('\n')
    input = ["{}".format(element.lstrip().rstrip()) for element in input]

    # trim off the heads and tails
    if input[0] == "":
        input.pop(0)
    if input[len(input)-1] == "":
        input.pop(len(input)-1)

    return input

def process_assignments(input):
    input = parse_input(input)

    result_part_1 = 0
    result_part_2 = 0
    for i in input:
        left_range, right_range = get_pair_ranges(i)
        if is_overlap(left_range, right_range):
            result_part_1 += 1
        if is_overlap_2(left_range, right_range):
            result_part_2 += 1
    return result_part_1, result_part_2

if __name__ == '__main__':
    f = open("input.txt", "r")
    output = f.read()
    result1, result2 = process_assignments(output)
    print(result1, result2)


# from pathlib import Path 

# lines = Path("input.txt").read_text().split()

# part1 = 0
# part2 = 0
# for line in lines:
#     e1, e2 = line.split(",")
#     a, b = map(int, e1.split("-"))
#     c, d = map(int, e2.split("-"))
#     if (a >= c and b <= d) or (a <= c and b >= d):
#         part1 += 1

#     if (
#         (a <= c <= b) or
#         (a <= d <= b) or
#         (c <= a <= d) or
#         (c <= b <= d)
#     ):
#         part2 += 1

# print(part1, part2)