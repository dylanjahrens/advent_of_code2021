with open("day1_input.txt", "r") as input_file:
    file_lines = input_file.readlines()
    input_list = [int(line.strip()) for line in file_lines] 

def day1_1():

    counter = 0
    
    for i, meas in enumerate(input_list):
        if i > 0:
            if meas > input_list[i-1]:
                counter +=1
    return counter


def day1_2():
    
    counter = 0
    
    for i, meas in enumerate(input_list):
        if i < len(input_list) - 3:
            a = input_list[i] + input_list[i+1] + input_list[i+2]
            b = input_list[i+1] + input_list[i+2] + input_list[i+3]
            if b > a:
                counter +=1
    return counter

