def read_into_lines(input):
    input = input.split('\n')
    input = ["{}".format(element.lstrip().rstrip()) for element in input]

    # trim off the heads and tails
    if input[0] == "":
        input.pop(0)
    if input[len(input)-1] == "":
        input.pop(len(input)-1)
    
    return input