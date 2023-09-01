age = int(input("what is your current age \n :"))
days = 365
weeks = 52
months = 12
day = age*days
week = age*weeks
month = age*months

days_remain = 90*365
week_remain = 90*52
month_remain = 90*12
x = days_remain-day
y = week_remain-week
z = month_remain- month
print(f"yours days remaing{x}, weeks remaining {y}, months remaimg {z}")

