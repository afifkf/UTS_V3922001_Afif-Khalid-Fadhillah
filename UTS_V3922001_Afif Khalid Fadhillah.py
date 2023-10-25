#!/usr/bin/env python
# coding: utf-8

# In[1]:


def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 0
            if char.islower():
                shift = ord('a')
            elif char.isupper():
                shift = ord('A')
            encrypted_char = chr(((ord(char) - shift + key) % 26) + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_cipher(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 0
            if char.islower():
                shift = ord('a')
            elif char.isupper():
                shift = ord('A')
            key_char = key[i % key_length]
            key_shift = 0
            if key_char.islower():
                key_shift = ord('a')
            elif key_char.isupper():
                key_shift = ord('A')
            encrypted_char = chr(((ord(char) - shift + (ord(key_char) - key_shift)) % 26) + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def encrypt(text, caesar_key, vigenere_key):
    caesar_encrypted = caesar_cipher(text, caesar_key)
    vigenere_encrypted = vigenere_cipher(caesar_encrypted, vigenere_key)
    return vigenere_encrypted

def decrypt(text, caesar_key, vigenere_key):
    vigenere_decrypted = vigenere_cipher(text, vigenere_key)
    caesar_decrypted = caesar_cipher(vigenere_decrypted, -caesar_key)
    return caesar_decrypted

text = "Success is not final, failure is not fatal, it is the courage to"
caesar_key = 91
vigenere_key = "AFIF"

# Enkripsi
encrypted_text = encrypt(text, caesar_key, vigenere_key)
print("Teks terenkripsi: " + encrypted_text)

# Dekripsi
decrypted_text = decrypt(encrypted_text, caesar_key, vigenere_key)
print("Teks terdekripsi: " + decrypted_text)


# In[ ]:




