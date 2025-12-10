from tables import initial_permutation,final_permutation
from functions import  permute,xor
from f_function import feistel

def decrypt(cipher,keys):
    block = permute(cipher,initial_permutation)
    l = block[:32]
    r = block [32:]
    for i in range (15,-1,-1):
        feistel_result = feistel(r,keys[i])
        l,r = r, xor(l,feistel_result)

    final = r + l
    return permute(final,final_permutation)


    