print("welcome to the pizza delivery")
pizza = input("which pizza do  u want s , m ,l\n :- ")
bill =0
if pizza == "s":
    bill += 100
    print(f"u r pizza of rs {bill}")
elif pizza == "m":
    bill  +=200
    print(f"u r pizzA OF RS {bill}")

else:
    bill +=300
    print(f"r r pizza of rs {bill}")


add_peproni =input("do u want peproni y or no \n :- ")
size = input("for which pizza do you want s , m l ")
if add_peproni =="y":
    if size == "s":
        bill+= 50
        print(f"u r total  bill is {bill}")
    else:
        bill +=100
        print(f" u r total bill is {bill}")

    bill += 50
    print(f"ur total bill is {bill}")
else:
    print(f"total bill is {bill}")


add_extra_cheese = input("do u want extra cheese y or no \n :- ")
if add_extra_cheese == "y":
    bill =+ 50
    print(f"u r total bill is {bill}")
else :
    bill+= 100
    print(f"u r total bill is {bill}")

print(f"your total bill is  {bill} ")
