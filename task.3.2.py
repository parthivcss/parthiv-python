a=int(input("enter a year"))
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print("given year is a leap year")
else:
    print("given year is not a leap year")
