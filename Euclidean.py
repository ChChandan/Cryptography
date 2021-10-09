
#Chandan Cherukuri
#Euclidean  algorithm

gcdarray=[]#globally declared array because if initialised inside the function then it would reset all the values when the function is called again
def euclidien(a,b):
    global gcdarray#defined a globar array to store the values of all reminders
    q=int(b/a)#To find the quotient of the division and convert into a whole number
    r=b%a#To find the reminder of the division
    if(r==0):#if the reminder is zero then it prints the last reminder which arrived before 0
        print("This GCD is "+ str(gcdarray[len(gcdarray)-1]))
        exit#it then exits the function
    else:
        gcdarray.append(r)#the reminders are added to the list one after another
        euclidien(r, a)#If  the reminder is not zero then the function is called again
a=1701
b=3768
euclidien(a,b)
