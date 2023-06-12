lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

armstrong_numbers = []
for number in range(lower_limit, upper_limit + 1):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_cubes = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_cubes == number:
        armstrong_numbers.append(number)
print("Armstrong numbers between", lower_limit, "and", upper_limit, "are:")
for armstrong_number in armstrong_numbers:
    print(armstrong_number)
