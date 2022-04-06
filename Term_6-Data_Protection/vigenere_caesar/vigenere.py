def vigenere_encrypt(word, key):
    n_alphabet = 26
    small_a = 97
    big_A = 65

    n_word = len(word)
    new_key = ''
    encrypted = ''

    i = 0
    while len(new_key) != len(word):
        new_key += key[i]
        i += 1
        if i == (len(key)):
            i = 0
    for i in range(len(word)):
        ch = word[i]
        k = new_key[i]
        base = big_A
        if ord(ch) > 96:
            base = small_a
        smallest = ch if ord(ch) < ord(k) else k
        diff = abs(ord(ch) - ord(k))
        encrypted += chr(((ord(smallest) + (ord(smallest) - base) - base + diff) % n_alphabet) + base)
    return encrypted


def vigenere_decrypt(encrypted, key):
    n_alphabet = 26
    small_a = 97
    big_A = 65

    n_word = len(encrypted)
    new_key = ''
    decrypted = ''

    i = 0
    while len(new_key) != len(encrypted):
        new_key += key[i]
        i += 1
        if i == (len(key)):
            i = 0
    for i in range(len(encrypted)):
        ch = encrypted[i]
        k = new_key[i]
        base = big_A
        if ord(ch) > 96:
            base = small_a
        decrypted += chr(((ord(ch) - base) - (ord(k) - base)) % n_alphabet + base)
    return decrypted
