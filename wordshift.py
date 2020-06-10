# Caesar cipher
text = input("Enter your message: ")
shift = int(input("Enter number of shifts: "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher+=char
        continue
    if char<='Z' and char>="A":
        code = ord(char) + shift
        if code > ord('Z'):
            code = code+ord('A')-ord('Z')-1
    elif ord(char)<=ord('z') and ord(char)>=ord("a"):
        code = ord(char) + shift
        if code > ord('z'):
            code = code+ord('a')-ord('z')-1
    cipher += chr(code)
print(cipher)