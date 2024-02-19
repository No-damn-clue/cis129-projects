#set constant values
coffee = 5
muffins = 4
#set text and inputs
coffeeAmount = int(input("How many coffees would you like?"))
muffinsAmount = int(input("How many muffins would you like?"))
#calculate total
totalCoffee = (coffee * coffeeAmount)
totalMuffins = (muffins * muffinsAmount)
total = (totalCoffee + totalMuffins)
tax = (total * 0.06)
totalAfterTax = (total + tax)
#display total
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffeeAmount)
print("Number of muffins bought?")
print(muffinsAmount)
print("***************************************")
print("")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(coffeeAmount ,"Coffee at $5 each: $" ,totalCoffee)
print(muffinsAmount ,"Muffins at $4 each: $" ,totalMuffins)
print("6% Tax: $" ,tax)
print("---------")
print("Total: $" ,total)
print("Total is ", totalAfterTax)
