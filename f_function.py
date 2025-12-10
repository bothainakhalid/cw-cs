from functions import permute,xor
from tables import expand,s_boxes,p_box

def s_box_substitutions(input_bits):
    result = ""
    for i in range(8): 
        blocks = input_bits[i*6:(i+1)*6] #divides bits into groups of 6
        column = int(blocks[1:5],2) # the middle four blocks identifies which column
        row = int (blocks[0]+blocks[5],2) #first and last bit identifies which row 
        value = s_boxes[i][row][column] #gets the value from the s boxes
        result +=f"{value:04b}" #converts the value to 4 bits and padded with zeros
    return result

def feistel(right_half, key):
    expanded = permute(right_half,expand) #performs expansion permutation
    x = xor(key,expanded) #XORs the 
    subs = s_box_substitutions(x)
    return permute(subs,p_box)
