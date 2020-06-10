from collections import *

str1=input("Enter String 1: ")
str2=input("Enter String 2: ")
for char in str1:
    frequencies = collections.Counter(str1)
x = frequencies.keys()
count=0
for char in frequencies:
    if char >=1:
        count+=1
if count==len(str):
    print("Yes")
else:
    print("No")