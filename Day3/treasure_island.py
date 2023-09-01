print("welcome to tresure island your mission find the treassure\n ")
print("        ____")
print("    ___/_____\___")
print("____|   ______    |____")
print("   |___|______|___|")


cross_road = input("you are at a cross road  take a road \n left or right \n : ")
if cross_road =="right":
    print("you come to the lake  there is aisalnd in the middle of the lake ")
    lake = input("take swim or wait \n : ")
    if lake == "wait":
        print("u r arrived to the island unharmed")
        door = input("choose the door\n red ,blue ,black \n:")
        if door == "blue":
            print("u won")
        elif door == "black":
            print("try agin")
        else:
            print("gameover")






    else:
        print("gameOver")







else:
    print("GAME OVER")
