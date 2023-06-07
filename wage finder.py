print("Welcome user!")
gen = input("Enter your gender: ")
age = int(input("Enter age: "))
days = int(input("Enter the number of days: "))

def wage(gen, days):
    if age >= 18 and age < 30 and gen == "M":
        sal = days * 700
        return sal
    elif age >= 18 and age < 30 and gen == "F":
        sal = days * 750
        return sal
    elif age >= 30 and age <= 40 and gen == "M":
        sal = days * 800
        return sal
    elif age >= 30 and age <= 40 and gen == "F":
        sal = days * 800
        return sal
    else:
        print("Age invalid")

print("Your salary is", wage(gen, days))
