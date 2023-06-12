def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_palindrome(number):
    number = str(number)
    reversed_number = number[::-1]
    return number == reversed_number

def count_digits(number):
    return len(str(number))

def main():
    input_number = int(input("Enter an integer: "))

    if input_number % 2 == 1:  # Odd number
        fact = factorial(input_number)
        num_digits = count_digits(fact)
        print(f"The factorial of {input_number} is: {fact}")
        print(f"The number of digits in the factorial is: {num_digits}")
    else:  # Even number
        if is_palindrome(input_number):
            print(f"{input_number} is a palindrome.")
        else:
            print(f"{input_number} is not a palindrome.")

main()
