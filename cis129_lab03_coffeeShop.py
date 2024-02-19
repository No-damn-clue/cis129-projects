#set constant values
coffee = 5
muffins = 4
croissant = 4
bacon = 2.5
#set text and inputs
coffeeAmount = int(input("How many coffees would you like?"))
muffinsAmount = int(input("How many muffins would you like?"))
croissantsAmount = int(input("How many croissants would you like?"))
baconAmount = int(input("How many bacon strips would you like?"))
#calculate total
totalCoffee = (coffee * coffeeAmount)
totalMuffins = (muffins * muffinsAmount)
totalCroissants = (croissant * croissantsAmount)
totalBacon = (bacon * baconAmount)
total = (totalCoffee + totalMuffins + totalCroissants + totalBacon)
tax = (total *0.06)
totalAfterTax = (total + tax)
#display total
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffeeAmount)
print("Number of muffins bought?")
print(muffinsAmount)
print("Number of croissant bought?")
print(croissantsAmount)
print("Number of bacon strips bought?")
print(totalBacon)
print("***************************************")
print("")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(coffeeAmount ,"Coffee at $5 each: $" ,totalCoffee)
print(muffinsAmount ,"Muffins at $4 each: $" ,totalMuffins)
print(croissantsAmount ,"Croissants at 4$ each: $" ,totalCroissants)
print(baconAmount ,"Bacon strips at 2.50$ each: $" ,totalBacon)
print("6% Tax: $" ,tax)
print("---------")
print("Total: $" ,total)
print("Total is ", totalAfterTax)
