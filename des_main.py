from keys import round_keys
from functions import bin_to_hexa,hexa_to_bin
from encrypt import encrypt
from decrypt import decrypt

plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"

plaintext_bin = hexa_to_bin(plaintext)
key_bin = hexa_to_bin(key)
keyss = round_keys(key_bin)
ciphertext_bin = encrypt(plaintext_bin,keyss)
decrypt_bin = decrypt(ciphertext_bin,keyss)

print(plaintext)
print(key)
print(bin_to_hexa(ciphertext_bin))
print(bin_to_hexa(decrypt_bin))