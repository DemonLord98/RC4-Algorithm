def swap_func(list, pos1, pos2):  
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

KEY = [1, 2, 3, 6]
PLAIN_TEXT = [1, 2, 2, 2]
ciphertext = []
# S_vector = list(range(0,256)) comment for now for testing purposes
S_vector = list(range(0,8))
T_vector = []
i, j= 0, 0
while i < len(S_vector):
    appe = KEY[i % len(KEY)]
    T_vector.append(appe)
    i += 1

i = 0

while i < len(S_vector):
    j = (j + S_vector[i] + T_vector[i]) % len(S_vector)
    swap_func(S_vector, i, j)
    i += 1

print (S_vector)
i, j, x= 0, 0, 0
while x < len(PLAIN_TEXT):
    i = (i + 1) % len(S_vector)
    j = (j + S_vector[i]) % len(S_vector)
    swap_func(S_vector, i, j)
    t = (S_vector[i] + S_vector[j]) % len(S_vector)
    key_mod = S_vector[t]
    appe = PLAIN_TEXT[x] ^ key_mod
    ciphertext.append(appe)
    x += 1

print(ciphertext)
