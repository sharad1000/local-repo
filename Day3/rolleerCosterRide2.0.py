print("welcome to the roler coster ride ")
height = int(input("tell me your height\n ::::::::::::::::::::::-"))
age = int(input("tell me your age\n::::::::::::::::::-"))
bill = 0
if height >= 120:
    print("u r eligble for a roller coster ride")
    if age <=12:
        bill = 7
        print("you have to pay 7$")
    elif age <=18:
        bill = 12
        print("you have to pay 12$")

    else :
        bill = 18
        print("you have to pay 18$")
    photo =input("if u want a photo u have to pay 7$ say y or n\:-")
    if photo == "y":
        bill += 7
        print(f"u have to pay {bill}$")
    else:
        print(f"u have to pay {bill}$")









else:
    print("u r not eligble so grow taller")