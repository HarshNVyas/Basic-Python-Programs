#32 is the diff + or - 

inp=input("Enter a string: ")
stc=inp.replace(" ","")
length=len(stc)
stc1=''

for i in range(length):
    stc1 += stc[length-i-1]
count=0
if stc1==stc:
    print("Palindrome")
else:
    for i in range(length):
        if stc[i]==stc1[i]:
            count+=1
        elif (ord(stc[i])-ord(stc1[i]))==32 or (ord(stc[i])-ord(stc1[i]))==-32:
            count+=1
    if count==(length):
        print("palindrome")
    else:
        print("Not a palindrome")