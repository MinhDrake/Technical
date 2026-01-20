def xor_decrypt(ciphertext, key):
    key_len = len(key)
    decrypted = ''.join(chr(ord(c) ^ ord(key[i % key_len])) for i, c in enumerate(ciphertext))
    return decrypted

ciphertext = "XwrlKzZubfyebiOqigy&*#"
key = "BlakeMitchell"
decrypted = xor_decrypt(ciphertext, key)
print(decrypted)