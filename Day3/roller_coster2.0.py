height = int(input("tell me u r height for a roler coster ride \n :- "))
if height >=120 :
    print("u r eligble for a ride ")

    age = int(input("tell me u r age \n :-  "))
    bill = 0
    if age <= 18:
        bill += 50
        print(f" u have to pay {bill}")
    elif age >= 60 and age <=100 :
        bill =0
        print(f" enjoy the ride from our side  {bill}")
    elif age > 18:
        bill = 100
        print(f" u have to pAY {bill} ")

else:
    print(" u r not elgible for a ride  ")





