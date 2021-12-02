#calculates love compatibility

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

def findFirstDigit(name1, name2):
    count = 0
    count = name1.lower().count("t")
    count += name1.lower().count("r")
    count += name1.lower().count("u")
    count += name1.lower().count("e")
    count += name2.lower().count("t")
    count += name2.lower().count("r")
    count += name2.lower().count("u")
    count += name2.lower().count("e")
    return str(count)
    
def findSecondDigit(name1, name2):
    count = 0
    count = name1.lower().count("l")
    count += name1.lower().count("o")
    count += name1.lower().count("v")
    count += name1.lower().count("e")
    count += name2.lower().count("l")
    count += name2.lower().count("o")
    count += name2.lower().count("v")
    count += name2.lower().count("e")
    return str(count)

loveMeter = int(findFirstDigit(name1, name2) + findSecondDigit(name1, name2))

if (loveMeter < 10 or loveMeter > 90):
    print(f"Your score is {loveMeter}, you go together like coke and mentos.")
elif (loveMeter > 40 and loveMeter < 50):
    print(f"Your score is {loveMeter}, you are alright together.")
else: print(f"Your score is {loveMeter}.")
