#Tip Calculator
print("Welcome to the tip calculator")
totBill = float(input("What was the total bill? $"))

tipPercent = int(input("What percentage tip you would like to give? 10, 12 or 15? "))

people = int(input("How many people to split the Bill? "))

tipDecimal = 1+(tipPercent/100)
amount = (totBill * tipDecimal)/people
SplitAmount = round(amount,2)

#this format gives two digit float values 
SplitAmount = "{:.2f}".format(amount)
print(f"Each person should pay: ${SplitAmount}")