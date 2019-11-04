import math

#dream job title
dream_job = input("What is your dream job title?\n")

#hourly wage want to earn
hourly_wage = input("How much hourly wage do you want to earn?\n")
try:
    wage = float(hourly_wage)
except:
    print("Please input integer of wage")   
else:
    #calculate the annual wage a year, paid 52 week
    annual_wage = float(wage * 8 * 5 * 52)
    print("Your annual wage is", annual_wage)

    #how much money for retirement
    retirement_saving = input("How much do you feel you will need at retirement time?\n")
    try:
        saving = float(retirement_saving)
    except:
        print("Please input interger of saving")
    #determin how many years thye have to work to save for retirement
    else:
        years_of_work = saving / annual_wage
        print("You need to work", math.ceil(years_of_work), "years")

        #number of work year is even or odd?
        even_or_odd = (math.ceil(years_of_work) % 2)
        print(even_or_odd)
        #print("if", even_or_odd, "is 0, then it is an even number, otherwise, it is an odd number")
        if even_or_odd > 0:
            print("The number is odd.")
        else:
            print("The number is even.")

        #print(year_even_odd)


