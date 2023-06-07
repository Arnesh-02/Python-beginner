"'Ratings willl be:1 is bad,2 is not bad,3 is average,4 is good and 5 is excellent'"
print("Hello user!")
food_rat=int(input("Enter food  rating(1-5)"))
service_rat=int(input("Enter service rating(1-5)"))
ambi_rat=int(input("Enter ambience rating(1-5)"))
bill=float(input("Enter bill amount:"))
def tips(food_rat,service_rat,ambi_rat):
    if food_rat==4 or food_rat==5:
        if service_rat==4 or service_rat==5:
            if ambi_rat==4 or ambi_rat==5:
                tips=bill*0.1
                return tips 
        if service_rat==1 or service_rat==2  or service_rat==3 :
            if  ambi_rat==1 or ambi_rat==2 or ambi_rat==3:
                tips=bill*0.05
                return tips
    if food_rat==1 or food_rat==2 or food_rat==3:
        if service_rat==4 or service_rat==5 :
            if  ambi_rat==4 or ambi_rat==5:
              tips=bill*0.05
              return tips
        if service_rat==1 or service_rat==2  or service_rat==3 :
            if  ambi_rat==1 or ambi_rat==2 or ambi_rat==3:
              tips=bill*0.01
              return tips
print("Tips=",tips(food_rat,service_rat,ambi_rat))
        
    
        


    









                
