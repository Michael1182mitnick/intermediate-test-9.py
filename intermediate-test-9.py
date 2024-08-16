# Write a function that repeatedly sums the digits of a number until a single-digit number is obtained.

def sum_digits_until_single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


# Example usage
number = int(input("Enter a number: "))
result = sum_digits_until_single_digit(number)
print(f"The single-digit result is: {result}")
