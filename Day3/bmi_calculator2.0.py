print("welcome to the bmi calculator")
weight = int(input("tell me your weight in kg\n :: "))
height = float(input("tell me your height in meter\n ::"))
bmi = round(weight/height**2)
print(bmi)
if bmi < 18.5:
    print("underweight")
elif bmi<18.5:
    print("normal")
elif bmi <25:
    print("u have normal weight")
elif bmi <30:
    print("u r over weight")
elif bmi < 35:
    print("obese")
else :
    print("clincally obese")