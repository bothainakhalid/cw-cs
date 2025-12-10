from tables import initial_permutation,final_permutation
from functions import  permute,xor
from f_function import fiestel

def decrypt(cipher,keys):
    block = permute(cipher,initial_permutation)
    l = block[:32]
    r = block [32:]
    for i in range (15,-1,-1):
        fiestel_result = fiestel(r,key[i])
        l,r = r, xor(l,fiestel_result)

    final = r + l
    return permute(final,final_permutation)