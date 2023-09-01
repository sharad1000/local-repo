print("welcome to the tip calculator")
bill = float(input("what was the total bill\n :"))
people = int(input("how mamy people to split the bill\n :"))
tip = int(input("what percentage tip would u like to give 10, 12 or 15\n :"))

tip_percent = float(tip/bill)*100
print(f"tip u want to give{tip_percent}")
total_bill = round(float(bill+tip_percent/people))
print(f"your total bill is {total_bill}")

