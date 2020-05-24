def utf8_list_to_int_list(list):
    encoding, errors = 'utf-8', 'surrogatepass'
    for item in range(len(list)):
        list[item] = int.from_bytes(list[item].encode(encoding, errors), 'big')
    return list


def swap(list, pos1, pos2):  
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list


def modify_S_vector(key, S_vector):
    T_vector, j = [], 0
    for i in range(len(S_vector)):
        appe = key[i % len(key)]
        T_vector.append(appe)
    
    for i in range(len(S_vector)):
        j = (j + S_vector[i] + T_vector[i]) % len(S_vector)
        swap(S_vector, i, j)

    return S_vector


def encrypt(plaintext_int, S_vector):
    cipher, i, j = [], 0, 0
    S_vector_mod = S_vector.copy()  # Create copy so the main S_vector is not modified
    for item in range(len(plaintext_int)):
        i = (i + 1) % len(S_vector_mod)
        j = (j + S_vector_mod[i]) % len(S_vector_mod)
        swap(S_vector_mod, i, j)
        t = (S_vector_mod[i] + S_vector_mod[j]) % len(S_vector_mod)
        key_mod = S_vector_mod[t]
        appe = plaintext_int[item] ^ key_mod
        cipher.append(appe)

    return cipher


def decrypt(cipher, S_vector):
    plaintext_int, i, j = [], 0, 0
    S_vector_mod = S_vector.copy()  # Create copy so the main S_vector is not modified
    for item in range(len(cipher)):
        i = (i + 1) % len(S_vector_mod)
        j = (j + S_vector_mod[i]) % len(S_vector_mod)
        swap(S_vector_mod, i, j)
        t = (S_vector_mod[i] + S_vector_mod[j]) % len(S_vector_mod)
        key_mod = S_vector_mod[t]
        appe = cipher[item] ^ key_mod
        plaintext_int.append(appe)

    return plaintext_int


plaintext = list(input("Enter text to be encrypted: "))
key = list(input("Enter the key: "))

plaintext = utf8_list_to_int_list(plaintext)
key = utf8_list_to_int_list(key)

S_vector = list(range(0,256))
S_vector_mod = modify_S_vector(key, S_vector)

print(plaintext)   # testing
cipher = encrypt(plaintext, S_vector_mod)
print(cipher)   # testing
plaintext = decrypt(cipher, S_vector_mod)
print(plaintext)   # testing

cipher_hex = list(map(hex, cipher))
for item in range(len(cipher_hex)):
    if len(cipher_hex[item]) == 3:
        cipher_hex[item] = cipher_hex[item].replace("0x", "0")

    else:
        cipher_hex[item] = cipher_hex[item].replace("0x", "")


cipher_hex_text = " ".join(cipher_hex)
print(f"\nCiphered text in Hex: \"{cipher_hex_text}\"")

