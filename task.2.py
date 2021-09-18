a=input("enter a string1")#parthiv
b=input("enter a string2")#pavan
status=0
if (len(a)==len(b)):
    for ch in a:
        if ch in b:
            status+=1
            continue
        else:
            print("it is not anagram")



if status==len(a):
    print("it is a anagram")
