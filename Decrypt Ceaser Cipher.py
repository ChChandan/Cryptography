def decrypt(ciphertext, key):
    if(len(ciphertext)==len(key)):
        plaintext = []
        for i in range(len(ciphertext)):
            x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
            x = x+65
            plaintext.append(chr(x))
        return("" . join(plaintext))
    else:
        print("key is not equal to the size of ciphertext")
ciphertext = "ZICVTWQNGKZEIIGASXSTSLVVWLA"
key = "DECEPTIVEWEAREDISCOVEREDSAV"
print("Plaintext  :",decrypt(ciphertext, key))
