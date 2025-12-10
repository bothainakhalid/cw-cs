from tables import pc1,pc2,shift_sched
from functions import left_shift,permute

def round_keys(main_key):
    sub_key = permute(main_key,pc1)
    left = sub_key[:28]
    right = sub_key[28:]
    final_key = []
#performs pc1 on the key which drops 8 parity keys making it 56 bits,
# then splits bits into left and right

    for s in shift_sched:
        left = left_shift(left, s)
        right = left_shift (right , s)
        full = left + right 
        final_key.append(permute(full,pc2))
    return final_key 
#performs shifting then performs pc2 to generate the final round key