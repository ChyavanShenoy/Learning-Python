# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Using FOR loop
highest_score = input
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The heighest_score in the class is {highest_score}")
