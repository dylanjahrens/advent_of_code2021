with open("day2_input.txt", "r") as input_file:
    file_lines = input_file.readlines()
    input_list = [line.strip() for line in file_lines]
    
split_list = []
for x in input_list:
    data = x.split(' ')
    split_list.append(data)
    
def day2_1():
    
    horizontal = 0
    depth = 0
        
    for inp in split_list:
        if inp[0] == 'up':
            depth -= int(inp[1])
        elif inp[0] == 'down':
            depth += int(inp[1])
        else:
            horizontal += int(inp[1])
    
    return horizontal * depth


def day2_2():
    
    aim = 0
    horizontal = 0
    depth = 0
    
    for inp in split_list:
        if inp[0] == 'up':
            aim -= int(inp[1])
        elif inp[0] == 'down':
            aim += int(inp[1])
        else:
            horizontal += int(inp[1])
            depth += aim * int(inp[1])
    
    return horizontal * depth

