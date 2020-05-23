def utf_8_to_int(text, encoding='utf-8', errors='surrogatepass'):
    integer = int.from_bytes(text.encode(encoding, errors), 'big')
    return integer


def create_int_list(list):
    for i in range(len(list)):
        list[i] = utf_8_to_int(list[i])
    return list


def swap_func(list, pos1, pos2):  
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list


plain_text = list(input("Enter text to be encrypted: "))
key = list(input("Enter the key: "))

plain_text = create_int_list(plain_text)
key = create_int_list(key)

S_vector = list(range(0,256))
T_vector = []
cipher = []
i, j = 0, 0
while i < len(S_vector):
    appe = key[i % len(key)]
    T_vector.append(appe)
    i += 1

i = 0
while i < len(S_vector):
    j = (j + S_vector[i] + T_vector[i]) % len(S_vector)
    swap_func(S_vector, i, j)
    i += 1

i, j, x = 0, 0, 0
while x < len(plain_text):
    i = (i + 1) % len(S_vector)
    j = (j + S_vector[i]) % len(S_vector)
    swap_func(S_vector, i, j)
    t = (S_vector[i] + S_vector[j]) % len(S_vector)
    key_mod = S_vector[t]
    appe = plain_text[x] ^ key_mod
    cipher.append(appe)
    x += 1


cipher_hex = list(map(hex, cipher))
for i in range(len(cipher_hex)):
    cipher_hex[i] = cipher_hex[i].replace("0x", "")

cipher_hex_text = " ".join(cipher_hex)
print(f"\nCiphered text in Hex: \"{cipher_hex_text}\"")

