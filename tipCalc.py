#Calculate total bill with tip
#Split bill

totalBill = input("How much is the total bill? ")

tipPercent = input("how much tip would you like to give? 10, 12, 15, or other? ")

totalPeople = input("How many to split the bill? ")

totalBill = float(totalBill)
tipPercent = int(tipPercent)
totalPeople = int(totalPeople)

splitTotal = round((totalBill * (tipPercent / 100 + 1)/totalPeople), 2)

print(f"Each person should pay {splitTotal}")
