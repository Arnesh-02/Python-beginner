start_table = int(input("Enter the start table: "))
end_table = int(input("Enter the end table: "))

for i in range(1, 11):  # Loop through numbers 1 to 10
    for j in range(start_table, end_table + 1):  # Loop through the given range
        print(f"{j} * {i} = {j * i}\t", end="")
    print()  # Move to the next line after each row
