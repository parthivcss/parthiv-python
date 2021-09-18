a="dogs"
b="cat"
dcount=0
ccount=0
for ch in a:
    dcount+=1
print(dcount)
for ch in b:
    ccount+=1
print(ccount)
if(dcount>ccount):
    print("dogs is largest string")
else:
    print("cat is larger string")
