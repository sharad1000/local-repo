import random
names_string = input("give me everybody  nmaes seprated by a comma\n :: - ")
names = names_string.split(", ")

# random.randint(0,x)
num_item = len(names)
random_choise = random.randint(0,num_item -1)
print(random_choise)
person_who_will_pay = names[random_choise]
print(person_who_will_pay+" is going to buy a meal today")

