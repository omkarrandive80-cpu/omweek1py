#7.Write a program to take a number as input and calculate the sum of all its digits.
n = int(input("Enter a number: "))  
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print("Sum of digits:", sum_of_digits)