# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# Using FOR loop

total_height = 0
student_count = 0
for height in student_heights:
    student_count += 1
    total_height += height
average_height = total_height / student_count
print(f"Average height: {average_height}")
