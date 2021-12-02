#calculates days, weeks, months left of life 
#based on a 90 year lifespan

age = int(input("What is your current age?"))

totalLifespan = 90 * 365
yourLifespan = int(age * 365)

monthsLeft = round((90 - age) * 12)
weeksLeft = round((90 - age) * 52)
daysLeft = round((90 - age) * 365)

print(f" You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left" )
