#set constant values
coffee = 5
muffins = 4
#set text and inputs
Coffee_amount = int(input("How many coffees would you like?"))
Muffins_amount = int(input("How many muffins would you like?"))
#calculate total
Total_amount = (coffee * Coffee_amount + muffins * Muffins_amount)
Total_after_tax = (Total_amount * 1.06)
#display total
print("Total is ", Total_after_tax)
