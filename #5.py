#5.Write a program to take a number as input and print all the even numbers from 1 to that number.

n = int(input("Enter a number: "))

print("Even numbers from 1 to", n, "are:")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)