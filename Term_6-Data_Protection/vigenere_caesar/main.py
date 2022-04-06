from caesar import *
from vigenere import *


shift = 99
word = 'ONEmoreEXAMPLE'
print('Caesar encryption:')
enc = caesar_encrypt(word, shift)
dec = caesar_decrypt(enc, shift)
print('word: ', word)
print('key', shift)
print('encrypted:', enc)
print('decrypted: ', dec)
print()

print('Vigenere encryption:')
key = 'LEMON'
word = 'ATTACKATDAWN'
enc = vigenere_encrypt(word, key)
dec = vigenere_decrypt(enc, key)
print('word: ', word)
print('key', key)
print('encrypted:', enc)
print('decrypted: ', dec)

