def breakupCalories(input):
    new_list = input.split('\n')
    new_list = ["{}".format(element.lstrip().rstrip()) for element in new_list]
    
    # Remove first entry if it's an empty value
    if len(new_list) > 0 and new_list[0] == "":
        new_list.pop(0)
    
    result = []
    current_list = []

    for item in new_list:
        if item == "":
            result.append(current_list)
            current_list = []
            continue
        current_list.append(int(item, 10))
    
    return result

def count_breakup(items):
    result = []
    sum = 0
    for item in items:
        for value in item:
            sum += value
        result.append(sum)
        sum = 0
    return result

def find_max(items):
    return max(items)

def listCalories(input):
    breakup_result = breakupCalories(input)
    count_results = count_breakup(breakup_result)
    max = find_max(count_results)
    return max

if __name__ == "__main__":
    f = open("input.txt", "r")
    output = f.read()
    max = listCalories(output)
    print(max)
