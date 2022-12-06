class DayFive:

    def build_tower(self, input):
        tower = []
        
        tower_split = input.split('\n')
        if tower_split[0] == "":
            tower_split.pop(0)
        if tower_split[len(tower_split)-1].lstrip().rstrip() == "":
            tower_split.pop(len(tower_split)-1)

        col = 1
        column_list = tower_split[len(tower_split)-1]
        while column_list.find(str(col)) >= 0:
            tower.append([])
            index = column_list.find(str(col))
            
            for i in range(0, len(tower_split) - 1):
                item = tower_split[i][index]
                if item != " ":
                    tower[col - 1].append(item)
            col += 1
        
        return tower
    
    def parse_instruction(self, instruction):
        instruction = instruction.replace('move ', '')
        num_items = instruction[0 : instruction.find(' from')].lstrip().rstrip()
        num_items = int(num_items)
        instruction = instruction[instruction.find('from ') + len('from '):]
        instruction = instruction.split(' to ')
        from_index = instruction[0]
        to_index = instruction[1]
        return num_items, int(from_index), int(to_index)

    def handle_instruction(self, tower, num_items, from_index, to_index):
        for i in range(0, num_items):
            # print('moving', i, tower[from_index-1][i])
            tower[to_index-1].insert(0, tower[from_index-1][i])
        for i in range(0, num_items):
            # print('pop result',tower[from_index-1])
            tower[from_index-1].pop(0)
        return tower

    def handle_instruction_2(self, tower, num_items, from_index, to_index):
        print('tower 1', tower, num_items, from_index, to_index)
        for i in range(num_items, 0, -1):
            # print('moving', i, tower[from_index-1][i])
            tower[to_index-1].insert(0, tower[from_index-1][i-1])
        for i in range(0, num_items):
            # print('pop result',tower[from_index-1])
            tower[from_index-1].pop(0)
        print('tower 2', tower)
        return tower

    def e2e_part1(self, input):
        input = input.split('\n\n')
        grid_data = input[0]
        instructions = input[1].split('\n')
        tower = self.build_tower(grid_data)
        for instruction in instructions:
            if instruction.lstrip().rstrip() == "":
                continue
            num_items, from_index, to_index = self.parse_instruction(instruction.lstrip().rstrip())
            # print('---', num_items, from_index, to_index, tower)
            tower = self.handle_instruction(tower, num_items, from_index, to_index)

        result = ''
        for i in tower:
            result += i[0]

        return result

    def e2e_part2(self, input):
        input = input.split('\n\n')
        grid_data = input[0]
        instructions = input[1].split('\n')
        tower = self.build_tower(grid_data)
        for instruction in instructions:
            if instruction.lstrip().rstrip() == "":
                continue
            num_items, from_index, to_index = self.parse_instruction(instruction.lstrip().rstrip())
            # print('---', num_items, from_index, to_index, tower)
            tower = self.handle_instruction_2(tower, num_items, from_index, to_index)

        result = ''
        for i in tower:
            result += i[0]

        return result
    
if __name__ == '__main__':
    part5 = DayFive()
    f = open("input.txt", "r")
    output = f.read()
    result = part5.e2e_part1(output)
    print('part 1', result)
    result = part5.e2e_part2(output)
    print('part 2', result)