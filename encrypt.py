from tables import initial_permutation,final_permutation
from functions import permute,xor
from f_function import fiestel

def encrypt(text,key):
    block = permute(text,initial_permutation)
    l = block[:32]
    r = block[32:]
    for i in range (16):
        fiestel_result = fiestel(r,key[i])
        l,r=r,xor(l,fiestel_result)
    
    final = r + l
    return permute(final, final_permutation)
