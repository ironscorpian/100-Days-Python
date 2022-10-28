
student_heights = input("Input a list of student heights ").split()

for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

for length in student_heights:
    result = student_heights.index(length)
    result+=result
    total_people = result - 1


sum = 0
for number in student_heights:
    sum = sum + number

average_height = round(sum / total_people)
print(average_height)

    




