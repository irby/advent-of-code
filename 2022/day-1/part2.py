from part1 import *

def find_top_3(list):
    list.sort(reverse=True)
    
    return [list[0], list[1], list[2]]

if __name__ == "__main__":
    f = open("input.txt", "r")
    output = f.read()
    breakup_result = breakupCalories(output)
    count_results = count_breakup(breakup_result)
    results = find_top_3(count_results)
    print(sum(results))
