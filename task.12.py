a=input("Enter a string")#parthiv423
dcount=0
chcount=0
for ch in a:
    if ch.isdigit():
        dcount+=1
    elif ch.isalpha():
        chcount+=1
    else:
        pass
print("no of digits in string:",dcount)
print("no of characters in string:",chcount)
