#check whether year is a leap year

year = int(input("Which year do you want to check? "))

def leapyear(year):
    if (year % 4 == 0) and (year % 100 != 0):
        if (year % 400 == 0):
            flag = True
        print("Leap year.")
    else: print("Not leap year.")

leapyear(year)
