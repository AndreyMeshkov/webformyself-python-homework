# Average Height
# Instructions
# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
# e.g.
#
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
# There are a total of 7 heights in student_heights
#
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
#
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
#
# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: 156, 178, 165, 171, 187
#
# Example Output
# 171
# e.g. When you hit run, this is what should happen:
#
# https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP
#
# Hint
# Remember to use the round() function to round the average height before you print it.
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:
#
# https://repl.it/@appbrewery/day-5-1-test-your-code
#
# This repl includes my testing code that will check if your code meets this assignment's objectives.
#
# Solution
# https://repl.it/@appbrewery/day-5-1-solution

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
count = 0
total_sum = 0
for i in student_heights:
    count += 1
    total_sum += i
avg = round(total_sum / count)
print(avg)

# Coach's solution

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
# print(average_height)
