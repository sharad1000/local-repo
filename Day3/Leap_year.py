print("to find the year is a leap year or normal year")
year = int(input("enter year  \n  ::-"))
modulo = year%4
if modulo == 0:
    print("this is a leap year")
else:
    print("this is a normal year")
