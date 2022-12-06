def find_marker_in_range(input, limit):
    index_found = limit
    for i in range(limit, len(input)):
        index_found += 1
        found_chars = []
        for j in range(0, limit):
            index = i - (limit-1-j)
            if input[index] not in found_chars:
                found_chars.append(input[index])
            else:
                break
            if j == (limit - 1):
                return index_found
        continue

def find_marker(input):
    return find_marker_in_range(input, 4)

def find_marker_2(input):
    return find_marker_in_range(input, 14)

if __name__ == '__main__':
    f = open("input.txt", "r")
    output = f.read()
    result = find_marker(output)
    print('part 1', result)
    result = find_marker_2(output)
    print('part 2', result)