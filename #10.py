#10.10. Write a program to create a function that takes a number as input and returns whether the number is even, odd, or prime.

def check_number(n):
    if n <= 1:
        return "Neither even, odd, nor prime"
    elif n == 2:
        return "Prime"
    elif n % 2 == 0:
        return "Even"
    else:
        is_prime = True
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            return "Prime"
        else:
            return "Odd"

# Test the function
print(check_number(2))   # Prime
print(check_number(4))   # Even
print(check_number(7))   # Prime
print(check_number(9))   # Odd