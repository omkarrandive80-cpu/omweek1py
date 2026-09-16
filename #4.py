#4.Write a program to take a student's marks as input and calculate the total, percentage, and grade based on the following criteria: A for 90+, B for 80-89, C for 70-79, D for 60-69, and F below 60.

marks = int(input("Enter the student's marks: "))

total = marks
percentage = marks

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("Total:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)