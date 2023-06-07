print("Welcome user!!")
def tax_fare(yr):
    if(yr>=60):
        fee=1020-((1020)*0.2)
        return fee
    else:
        fee=1020
        return fee
b_yr=int(input("Enter your year of birth:"))
yr=2023-b_yr
print("Travelling charge would be,rs",tax_fare(yr))
