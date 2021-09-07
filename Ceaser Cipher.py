
text = "PHHW PH DIWHU WKH WRJD SDUWB"
key = -3
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
print( final)
      
    



