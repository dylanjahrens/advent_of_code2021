with open("day3_input.txt", "r") as input_file:
    file_lines = input_file.readlines()
    input_list = [line.strip() for line in file_lines]
    
def day3_1():
    
    g = ''
    e = ''
    index = 0
    
    while index < len(input_list[0]):
        g0 = 0
        g1 = 0
        for inp in input_list:
            if inp[index] == '0':
                g0 +=1
            else:
                g1 +=1
        if g0 > g1:
            g += '0'
            e += '1'
        else:
            g += '1'
            e += '0'
        index +=1
        g0 = 0
        g1 = 0
    
    g_dec = int(g,2)
    e_dec = int(e,2)
    
    power_consumption = g_dec * e_dec
    
    return power_consumption

def day3_2():
    
    ogr = input_list
    co2 = input_list
    ogr_index = 0
    co2_index = 0

    while len(ogr) > 1:
        ogr1 = 0
        ogr0 = 0
        for inp in ogr:
            if inp[ogr_index] == '1':
                ogr1+=1
            else:
                ogr0+=1
        if ogr1 >= ogr0:
            ogr = [inp for inp in ogr if inp[ogr_index] == '1']
        else:
            ogr = [inp for inp in ogr if inp[ogr_index] == '0']
        ogr_index +=1
        ogr1 = 0
        ogr0 = 0
    
    while len(co2) > 1:
        co21 = 0
        co20 = 0
        for inp in co2:
            if inp[co2_index] == '1':
                co21+=1
            else:
                co20+=1
        if co20 <= co21:
            co2 = [inp for inp in co2 if inp[co2_index] == '0']
        else:
            co2 = [inp for inp in co2 if inp[co2_index] == '1']
        co2_index +=1
        co21 = 0
        co20 = 0
    
    ogr_str = ''
    co2_str = ''
    for n in ogr:
        ogr_str +=n
    for n in co2:
        co2_str +=n
   
    ogr_dec = int(ogr_str,2)
    co2_dec = int(co2_str,2)
    
    lsr = ogr_dec * co2_dec
    
    return lsr