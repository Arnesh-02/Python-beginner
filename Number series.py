n = int(input("Enter a number: "))

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

series_sum = 0

for i in range(1, n + 1):
    term = i / factorial(i)
    series_sum += term

print("Sum of the series:", series_sum)

