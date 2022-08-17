# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


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

concat_string = int(str(true) + str(love))

if (concat_string < 10) or (concat_string > 90):
    print(
        f"Your score is {concat_string}, you go together like coke and mentos.")
elif (concat_string >= 40) and (concat_string <= 50):
    print(f"Your score is {concat_string}, you are alright together.")
else:
    print(f"Your score is {concat_string}")
