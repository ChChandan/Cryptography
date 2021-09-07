def decrypt(message):
    givenmap = {'A' : 'A', 'B' : 'N', 'C' : 'D', 'D' : 'R', 'E' : 'E',
        'F' : 'W', 'G' : 'I', 'H' : 'C', 'I' : 'K', 'J' : 'S',
        'K' : 'O', 'L' : 'H', 'M' : 'T', 'N' : 'B', 'O' : 'F',
        'P' : 'G', 'Q' : 'J', 'R' : 'L', 'S' : 'M', 'T' : 'P',
        'U' : 'Q', 'V' : 'U', 'W' : 'V', 'X' : 'X', 'Y' : 'Y',
        'Z' : 'Z'}
    plaintext=''
    for i in message:
        plaintext+=givenmap[i]
    return plaintext



ciphertext = "SEEMSEAOMEDSAMHL"
print(decrypt(ciphertext))
