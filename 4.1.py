import random
print("ludo game\n")
uk_flag = """
  __| __| __| __| __| __| __| __|
 |__ |__ |__ |__ |__ |__ |__ |__ |
  __| __| __| __| __| __| __| __|
 |__ |__ |__ |__ |__ |__ |__ |__ |
  __| __| __| __| __| __| __| __|
 |__ |__ |__ |__ |__ |__ |__ |__ |
  __| __| __| __| __| __| __| __|
 |__ |__ |__ |__ |__ |__ |__ |__ |
               |__ |
               |__ |
"""
print(uk_flag)



dice = random.randint(1,6)
if dice == 1:
    print("you got ----- one")
elif dice == 2:
    print("you got ------ two ")
elif dice == 3:

    print("you got ------------ three")
elif dice == 4:
    print("you got ------ four ")
elif dice == 5:
    print("you got ------ five ")
elif dice == 6:
    print("you got ------ six ")
elif dice == 7:
    print("you got ------ seven ")
elif dice == 8:
    print("you got ------ eight ")