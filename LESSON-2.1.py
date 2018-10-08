from os import system, name

def clear():
	# Windows
    if name == 'nt': 
        _ = system('cls') 
    # Mac and Linux
    else: 
        _ = system('clear') 

def calculateOrder(drinkName):
	print("\nYour order is complete. Please view the receipt below. Thank you for using Dominos® Online Ordering System!\n")
	print("" + name + " ORDERED " + orderAmount + " PIZZAS, EACH CONTAINING " + peperroniAmount + " PEPERRONIS AND " + oliveAmount + " OLIVES.")
	print("DRINK - " + drinkName + ".\n")

	print("---------------\n\nINDIVIDUAL RECEIPTS - \n")

	for x in range(int(orderAmount)):
		print("" + name + " ORDERED 1 PIZZAS CONTAINING " + peperroniAmount + " PEPERRONIS AND " + oliveAmount + " OLIVES.")

	print("\nDRINK - " + drinkName + ".\n")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        return False

clear()

print("Hello! Please enter your name - ")
name = input("")

print("\nWelcome to Dominos® Online Ordering System. How many pizzas will you order today?")
orderAmount = input("ANSWER - ")

while is_number(orderAmount) != True:
	print("\nThat is not a valid number. Please try again.")
	orderAmount = input("ANSWER - ")

print("\nNow please select your toppings. If you do not want any toppings, enter '0' for the number")	
peperroniAmount = input("PEPPERONI - ")

while is_number(peperroniAmount) != True:
	print("\nThat is not a valid number. Please try again.")
	peperroniAmount = input("ANSWER - ")

oliveAmount = input("\nOLIVES - ")

while is_number(oliveAmount) != True:
	print("\nThat is not a valid number. Please try again.")
	oliveAmount = input("ANSWER - ")

print("\nWould you also like to order a drink?\n A. YES\n B. NO\n*NOTE - Please use a capital letter to describe you answer.\n")
drinkOption = input("ANSWER - ")

while drinkOption != "A" and drinkOption != "B":
	print("\nThat is not an option. Please try again.")
	drinkOption = input("ANSWER - ")

if (drinkOption == "A"):
	print("\nWhich drink do you want to order?\n A. PEPSI\n B. SPRITE\n C. WATER")
	drinkName = input("ANSWER - ")

	while drinkName != "A" and drinkName != "B" and drinkName != "C":
		print("\nThat is not an option. Please try again.")
		drinkName = input("ANSWER - ")

	if drinkName == "A":
		calculateOrder("PEPSI")
	elif drinkName == "B":
		calculateOrder("SPRITE")
	elif drinkName == "C":
		calculateOrder("WATER")

elif (drinkOption == "B"):
	calculateOrder("NONE")