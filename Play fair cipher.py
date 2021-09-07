def encryption(plaintext,ciphermatrix):
    x=0
    y=2
    ciphertext=[]
    while y <= len(plaintext):
        keyword=plaintext[x:y]
        firstword=[]
        secondword=[]
        finalword=[]
        for a in range(len(ciphermatrix)):
            for b in range(len(ciphermatrix)):
                if(keyword[0:1]==ciphermatrix[a][b]):
                    firstword+=[a,b]
                if(keyword[1]==ciphermatrix[a][b]):
                    secondword+=[a,b]
                        
        finalword.append(firstword)
        finalword.append(secondword)
        c=finalword[0][0]
        d=finalword[0][1]
        e=finalword[1][0]
        f=finalword[1][1]
        if(c == e):
            if(f+1==len(ciphermatrix) or d+1==len(ciphermatrix) ):
                ciphertext+=ciphermatrix[c][0]
                ciphertext+=ciphermatrix[e][0]
            else:
                 ciphertext+=ciphermatrix[c][f+1]
                 ciphertext+=ciphermatrix[e][d+1]

        elif(d == f):
                if(c+1==len(ciphermatrix) or e+1==len(ciphermatrix) ):
                    ciphertext+=ciphermatrix[0][f]
                    ciphertext+=ciphermatrix[0][d]
                else:
                    ciphertext+=ciphermatrix[c+1][f]
                    ciphertext+=ciphermatrix[e+1][d]
        else:
            ciphertext+=ciphermatrix[c][f]
            ciphertext+=ciphermatrix[e][d]
        ciphertext="".join(ciphertext)
        x+=2
        y+=2
    return(ciphertext)

def validation(ciphermatrix,plaintext):
    if((len(plaintext))%2==0):
        print("This is the cipher text "+ encryption(plaintext,ciphermatrix))
    else:
        plaintext=plaintext+'x'
        print("This is the cipher text "+ encryption(plaintext,ciphermatrix))

def matrixgeneration():
    key=input("enter key")
    Lol=[]
    for x in key.upper():
        if x not in Lol:
            Lol.append(x)
    alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in alphabets:
        if x not in Lol:
            Lol.append(x)
    key_matrix=[Lol[0:5],Lol[5:10],Lol[10:15],Lol[15:20],Lol[20:25]]
    print(key_matrix)

ciphermatrix=[
["s","r","m","a","p"],
["u","n","i","v","e"],
["t","y","b","c","d"],
["f","g","h","k","l"],
["o","q","w","x","z"]
]

plaintext="wearediscoveredsaveyourself"
#matrixgeneration()
validation(ciphermatrix, plaintext)
