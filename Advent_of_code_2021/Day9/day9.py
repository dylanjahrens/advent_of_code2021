with open("day9_input.txt", "r") as input_file:
    file_lines = input_file.readlines()
    input_list = [data.split() for data in file_lines]
    hm = []
    for l in input_list:
        hm_line = []
        for s in l:
            for n in s:
                hm_line.append(int(n))
        hm.append(hm_line)

test = [[2,1,9,9,9,4,3,2,1,0],[3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],[8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]]

        
def p1(data):
    
    low_points = []

    #top corners
    if data[0][0] < data[0][1] and data[0][0] < data[1][0]:
        low_points.append(data[0][0])
    if data[0][-1] < data[0][-2] and data[0][-1] < data[1][-1]:
        low_points.append(data[0][-1])
    
    #bottom corners
    if data[-1][0] < data[-1][1] and data[-1][0] < data[-2][0]:
        low_points.append(data[-1][0])
    if data[-1][-1] < data[-1][-2] and data[-1][-1] < data[-2][-1]:
        low_points.append(data[-1][-1])
        
    #top row
    for i, n in enumerate(data[0][1:-1],1):
        if n < data[0][i-1] and n < data[0][i+1] and n < data[1][i]:
            low_points.append(n)
            
    #bottom row
    for i, n in enumerate(data[-1][1:-1],1):
        if n < data[-1][i-1] and n < data[-1][i+1] and n < data[-2][i]:
            low_points.append(n)
            
    #left and right column
    for i, line in enumerate(data[1:-1],1):
        if line[0] < data[i-1][0] and line[0] < line[1] and line[0] < data[i+1][0]:
            low_points.append(line[0])
        if line[-1] < data[i-1][-1] and line[-1] < line[-2] and line[-1] < data[i+1][-1]:
            low_points.append(line[-1])
            
    for li, line in enumerate(data[1:-1],1):
        for ni, num in enumerate(line[1:-1],1):
            if (num < line[ni-1] and num < line[ni+1] and
                num < data[li-1][ni] and num < data[li+1][ni]):
                low_points.append(num)
                
    #print(low_points)
    
    #risk
    return sum(low_points) + len(low_points)

p1(hm)