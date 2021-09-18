a=input("Enter a string")
sm=0
for ch in a:
    if ch.isdigit():
        sm+=int(ch)
print(sm)
