def encryption(text,key):
    result = ""
    final=""
    for i in range(len(text)):
        word = text[i]
        if (word.isupper()):
            result += chr((ord(word) + key-65) % 26 + 65)
        elif(word==" "):
            result += " "
        else:
            result += chr((ord(word) + key - 97) % 26 + 97)
        
        if(result=="k"):
           final=final+" "
        else:
           final=result
    print(final)

def decryption(ciphertext, key):
    if(len(ciphertext)==len(key)):
        plaintext = []
        for i in range(len(ciphertext)):
            x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
            x = x+65
            plaintext.append(chr(x))
        return("" . join(plaintext))
    else:
        print("key is not equal to the size of ciphertext")

      
    
text = "PHHW PH DIWHU WKH WRJD SDUWB"
key = -3
encryption(text,key)
ciphertext = "ZICVTWQNGKZEIIGASXSTSLVVWLA"
key = "DECEPTIVEWEAREDISCOVEREDSAV"
print("Plaintext  :",decryption(ciphertext, key))


