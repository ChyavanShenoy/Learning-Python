# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12

print("This program will calculate the bill for a restaurant.")
bill = float(input("Please enter the bill amount. "))
people = int(input("Please enter the number of people. "))
tip = int(input("Please enter the tip percentage. 10, 12, 15, or 18. "))
bill_per_person = round((bill / people) * (1 + (tip / 100)), 2)
print(f"Each person should pay ${bill_per_person}.")
