def dissect_compartments(input):
    input_len = len(input)
    compartment_len = int(input_len / 2)
    first_compartment = input[0:compartment_len]
    second_compartment = input[compartment_len:]
    return first_compartment, second_compartment

def find_similarities(first_compartment, second_compartment):
    return ''.join(set(first_compartment).intersection(second_compartment))

def rank_priority(input):
    if input >= 'a' and input <= 'z':
        return (ord(input) - ord('a'))+1
    if input >= 'A' and input <= 'Z':
        return (ord(input) - ord('A'))+27

def process_rucksack(input):
    input = input.split('\n')
    input = ["{}".format(element.lstrip().rstrip()) for element in input]

    result = 0

    for line in input:
        if line == "":
            continue
        first_compartment, second_compartment = dissect_compartments(line)
        similarity = find_similarities(first_compartment, second_compartment)
        priority = rank_priority(similarity)
        result += priority
    
    return result

if __name__ == '__main__':
    f = open("input.txt", "r")
    output = f.read()
    result = process_rucksack(output)
    print(result)