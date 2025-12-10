from functions import permute,xor
from tables import expand,s_boxes,p_box

def s_box_substitutions(input_bits):
    result = ""
    for i in range(8):
        blocks = input_bits[i*6:(i+1)*6]
        column = int(blocks[1:5],2)
        row = int (blocks[0]+blocks[5],2)
        value = s_boxes[i][row][column]
        result +=f"{value:04b}"
    return result

def fiestel(right_half, key):
    expanded = permute(right_half,expand)
    x = xor(key,expanded)
    subs = s_box_substitutions(x)
    return permute(subs,p_box)
