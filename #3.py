#3.Write a program to take three numbers as input and print the largest and smallest number among them.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
largest=max(a, b, c)
smallest=min(a, b, c)
print("The largest number is:", largest)
print("The smallest number is:", smallest)