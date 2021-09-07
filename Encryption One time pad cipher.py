import random#random library is imported to generate the random number

def onetimepadcipher(key):
    finalkey=list()
    codeword=''
    keyword=''
    for i in key:
        n=random.randint(0,26)# random number between 0-26 is generated for each specific charecter
        finalkey.append(n)#random number store in n will be added to the list
    
        #ciphertext=((ord(i)+n)%26)+65
        codeword += chr(((ord(i)+n)%26)+65)#the random number that is generated for this specific charecter is used to encrpyt the message
        #print(ciphertext)

    
    print("This is the codeword: "+str(codeword))
    print("This is the one time key : "+str(finalkey))
    decrypt(finalkey,codeword)

def decrypt(key,ciphertext):
    plaintext=''
    for x in range(len(key)) :
        plaintext+= chr(((ord(ciphertext[x])-key[x])%26)+65)

    print(" \nThis is the original plain text "+str(plaintext))
        

onetimepadcipher("WEWISHTOREPLACEPLAYER")
    





