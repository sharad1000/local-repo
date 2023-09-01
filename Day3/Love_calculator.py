name1 = input("Tell me the name1:\n")
name2 = input("Tell me the name2:\n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

love_score = true * 10 + love

print(f"Your love score is {love_score}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}. You go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print("Your score is y.")
