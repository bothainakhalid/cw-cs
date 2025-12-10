def permute(block,table):
    return "".join(block[i-1] for i in table)
#permutation function

def xor(a,b):
    return "".join("1" if a[i]!=b[i] else "0" for i in range (len(a)))
#xor function

def left_shift(bits, num):
    return bits[num:]+bits[:num]
#left shift function for key generation 

def bin_to_hexa(b):
    return f"{int(b,2):016X}"
#converting binary to hexadecimal

def hexa_to_bin(h):
    return f"{int(h,16):064b}"
#converting hexadecimal to binary