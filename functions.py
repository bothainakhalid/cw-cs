def permute(block,table):
    return "".join(block[i-1] for i in table)

def xor(a,b):
    return "".join("1" if a[i]!=b[i] else "0" for i in range )