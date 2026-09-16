#Write a program to take a number as input and calculate the factorial of that number using a loop.
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is:", factorial)