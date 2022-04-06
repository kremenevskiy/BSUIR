def caesar_encrypt(word, shift):
    n_alphabet = 26
    small_a = 97
    big_A = 65
    encrypted = ''
    for ch in word:
        base = big_A
        if ord(ch) > 96:
            base = small_a
        encrypted += chr(((ord(ch) - base + shift) % n_alphabet) + base)
    return encrypted


def caesar_decrypt(encrypted, shift):
    n_alphabet = 26
    small_a = 97
    big_A = 65
    decrypted = ''
    for ch in encrypted:
        base = big_A
        if ord(ch) > 96:
            base = small_a
        decrypted += chr((ord(ch) - base - shift + n_alphabet) % n_alphabet + base)
    return decrypted