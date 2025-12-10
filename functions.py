def permute(block,table):
    return "".join(block[i-1] for i in table)

def xor(a,b):
    return "".join("1" if a[i]!=b[i] else "0" for i in range (len(a)))

def left_shift(bits, num):
    return bits[num:]+bits[:num]

def bin_to_hexa(b):
    return f"{int(b,2):016X}"

def hexa_to_bin(h):
    return f"{int(h,16):064b}"