#4.Write a program to take a student's marks as input and calculate the total, percentage, and grade based on the following criteria: A for 90+, B for 80-89, C for 70-79, D for 60-69, and F below 60.
#if we take marks input of 3 students, we can calculate the total marks, percentage, and grade for each student. Here's a sample code to achieve this:

marks1 = int(input("Enter the first student's marks: "))
marks2 = int(input("Enter the second student's marks: "))
marks3 = int(input("Enter the third student's marks: "))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100    

if percentage >= 90:
    print("a")
elif percentage >= 80:
    print("b")
elif percentage >= 70:
    print("c")
elif percentage >= 60:
    print("d")
else:
    print("f")

print("Total:", total)
print("Percentage:", percentage, "%")
