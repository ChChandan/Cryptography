#Chandan Cherukuri 
#S-DES Encryption Algorithm

def permutator(key,permutationcommand):
    if(permutationcommand==1):
        givenpermutation=[3,5,2,7,4,10,1,9,8,6]#first permutation
    elif(permutationcommand==2):
        givenpermutation=[6,3,7,4,8,5,10,9]#second permutation
    elif(permutationcommand==3):
        givenpermutation=[2,6,3,1,4,8,5,7]#intial permutation
    elif(permutationcommand==4):
        givenpermutation=[4,1,2,3,2,3,4,1]#expansion permutation
    elif(permutationcommand==5):
        givenpermutation=[2,4,3,1]#P4 permutation
    elif(permutationcommand==6):
        givenpermutation=[4,1,3,5,7,2,8,6]# inverse initial permutation
    else:
        exit 
    
    for z in range(len(givenpermutation)):
        givenpermutation[z]=givenpermutation[z]-1
    
    newkey=[]
       
    for x in givenpermutation:
        newkey+=key[x]
    return newkey
def XOR(x, y):
	result = []

	for i in range(0, len(y)):
		if x[i] == y[i]:
			result.append('0')
		else:
			result.append('1')

	return result
def leftshift(fivebitkey):
    tempbit=''
    tempbit=fivebitkey[4]
    fivebitkey.pop()
    fivebitkey.insert(0,tempbit)
    return fivebitkey
def find( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 *
                find(int(decimal_number // 2)))

def Sbox(s0,s1):
    #defining matrix of S0 and S1
    s0_matrix=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1_matrix=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    #Taking the last and first bits to find the row and middle two bits to find column
    s0_row=s0[0]+s0[3]
    s0_column=s0[1]+s0[2]
  
    #converting the bits from binary to decimal
    s0_row=int(s0_row,2)
    s0_column=int(s0_column,2)
    #Taking the last and first bits to find the row and middle two bits to find column
    s1_row=s1[0]+s1[3]
    s1_column=s1[1]+s1[2]

    
    #converting the bits from binary to decimal
    s1_row=int(s1_row,2)
    s1_column=int(s1_column,2)
    
    #Finding the position of S0 matrix and S1 matrix
    s0_output=s0_matrix[s0_row][s0_column]
    s1_output=s1_matrix[s1_row][s1_column]


    #Converting the output from decimal to binary 

    if(s0_output==1):
        s0_output='01'
    else:
        s0_output=find(s0_output)

    if(s1_output==1):
        s1_output='01'
    else:
        s1_output=find(s1_output)
 
    #Converting the output from string to array    
    s0_final=[x for x in str(s0_output)]
    s1_final=[x for x in str(s1_output)]  
    
    #Taking the sum of the left and right bits
    finalword=s0_final+s1_final
   


    #Performing the P4 permutation
    finalword=permutator(finalword,5)

    #returning the output
    return finalword

def keygenerator(key):
    key_1=[]
    key_2=[]
    print("The intial given key : "+key)
   
    codeword = [x for x in key]
    codeword=permutator(codeword,1)
   
    fivebit_1=codeword[0:5]
    fivebit_2=codeword[5:10]
   
    codeword="".join(codeword)
    print("This is the key after permutation :"+codeword)
   
    leftshift_1=leftshift(fivebit_1)
    leftshift_2=leftshift(fivebit_2)
   
    key_1=leftshift_1+leftshift_2
    key_1=permutator(key_1,2)
    key_1 = "".join(key_1)
    print("This is the K1 : "+key_1)

    leftshift_3=leftshift(leftshift_1)
    leftshift_4=leftshift(leftshift_2)
   
    key_2=leftshift_3+leftshift_4
    key_2=permutator(key_2,2)
   
    key_2 = "".join(key_2)
    print("This is the K2 : "+key_2)
    
    return key_1,key_2
    #encryption(key_1, key_2,plaintext)
    



def encryption(key,plaintext):
    codeword=plaintext
    #splitting codeword
    left=codeword[0:4]
    right=codeword[4:8]
    #Right to Expansion permutation
    newword=permutator(right,4)
    #Perform XOR operation with Key 1
    newword=XOR(newword,key)
    #splitting word
    newleft=newword[0:4]
    newright=newword[4:8]
    lastword=Sbox(newleft,newright)
    lastword=XOR(left,lastword)
    return lastword,right

def swap(left,right):
    temp=left
    left=right
    right=temp
    return left,right

def brain(key,plaintext):
    #Key generation
    key1,key2=keygenerator(key)
    codeword = [x for x in plaintext]
    #initial permutation
    codeword=permutator(codeword, 3)
    #First step encryption
    firstflip,right=encryption(key1,codeword)
    #swapping variables
    left,right=swap(firstflip,right)
    secondflip=left+right
    #Second step encryption
    secondflip,right=encryption(key2,secondflip)
    ciphertext=secondflip+right
    #Inverse Initial permutation
    ciphertext=permutator(ciphertext,6)
    ciphertext="".join(ciphertext)
    print("This is the cipher text "+ciphertext)
    
    

    
plaintext = "01101101"
key="1011000100"
brain(key,plaintext)

