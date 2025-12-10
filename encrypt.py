from tables import initial_permutation,final_permutation
from functions import permute,xor
from f_function import feistel

def encrypt(text,key):
    block = permute(text,initial_permutation) #performs initial permutation
    l = block[:32] #left side
    r = block[32:] #right side
    for i in range (16): #loop for 16 rounds
        feistel_result = feistel(r,key[i]) 
        l,r=r,xor(l,feistel_result) #the new l is old r and the new r is the old l XORed with feistel result
    
    final = r + l #swapping left and right
    return permute(final, final_permutation) #final permutation
