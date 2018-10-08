# FUNCTIONS

def lessonTwo_one (name, pizzaNumber, peperroni, olives, drink):
	print(name + " ordered " + str(pizzaNumber) + " pizzas with " + str(peperroni) + "peperronis and " + str(olives) + "olives.")
	print("DRINK - " + drink)

def lessonTwo_two (x, y, z):
	average = (x+y+z) / 3
	print("The average of those three numbers is " + str(average))

def lessonFour_one (list):
	list = "This list is now a string."
	print(list)

def lessonFive (age):
	if int(age) >= 14:
		print(" JOIN ROBOTICS TEAM")
	if int(age) >= 16:
		print(" DRIVE AND HAVE A JOB")
	if int(age) >= 18:
		print(" ATTEND COLLEGE")
	if int(age) >= 21:
		print(" BE AN ADULT")
	if int(age) >= 35:
		print(" BECOME PRESIDENT")
	elif int(age) < 14:
		print("Nothing from our list.")
	else:
		# Print nothing. This "else" statement will never be called.
		print("")

def lessonSeven_one (word):
	words = ["Burger", "Pizza", "Hot Dog", "Corn Dog", "Chicken Nuggets", "French Fries", "Onion Rings", "Fried Chicken", "Sandwich", "Soda"]

	if word in words:
		print("\nThis word already exists.")

	else:
		words.append(word)
		print("\n'" + word + "' has been added to the array. Here is the full array - ")
		print(words)

def lessonSeven_two (name, color, pets):
	userinfo = []

	userinfo.append(name)
	userinfo.append(color)
	userinfo.append(numberOfPets)

	print("Thank you for complying with this required NSA Data Collection Program! Here is some of the data we collected -\n NAME - " + str(userinfo[0]) + "\n FAVORITE COLOR - " + str(userinfo[1]) + "\n NUMBER OF PETS - " + str(userinfo[2]))

def lessonSeven_three (password):
	bankAccounts = {
		"893758": "5678",
		"978479": "78303",
		"126743": "368",
		"386090": "6540",
		"658673": "1200500",
		"204796": "52",
		"793856": "8907",
		"427594": "13901",
		"173901": "2794",
		"230986": "2460",
	}

	print("\nAccount " + code + " contains " + str(bankAccounts.get(code)) + " dollars. Would you like to...\n A. DELETE THIS ACCOUNT\n B. ADD NEW ACCOUNT\n C. QUIT APPLICATION\n")
	accountOptions = input("ANSWER - ")

	while accountOptions != "A" and accountOptions != "B" and accountOptions != "C":
		accountOptions = input("That is not a valid option. Please try again - ")

	if accountOptions == "A":
		bankAccounts.pop(code)
		print("That account has been deleted. Thank you for using the CHASE® Online Banking System.")

	elif accountOptions == "B":
		newAccountKey = input("\nEnter the new six-digit account code - ")
		newAccountValue = input("How much money will be located in this account - ")

		bankAccounts[newAccountKey] = str(newAccountValue)
		print("\nThat account has been created. Thank you for using the CHASE® Online Banking System.\nHere is the new account -\n CODE: " + newAccountKey + "\n VALUE: " + str(bankAccounts.get(newAccountKey)))

def lessonEight_one (word):
	array = []
	array.append(word)

	while word != "STOP":
		array.append(word)

		print("\nThat word has been added to the array. Please enter another word.")
		word = input("WORD - ")

	print("\nYou have selected 'STOP'. Here is the array we created - ")
	print(str(array))


def lessonEight_two (array):
	reversedArray = []

	print("Original Array - " + str(array))

	for x in range(0, len(array)):
		reversedArray.append(array[(int(len(array)))-1 - x])

	print("Original Array - " + str(reversedArray))

def lessonEight_one (word):
	array = []

	while word != "STOP":
		array.append(word)

		print("\nThat word has been added to the array. Please enter another word.")
		word = input("WORD - ")

	print("\nYou have selected 'STOP'. Here is the array we created - ")
	print(str(array))

def lessonEight_two (array):
	reversedArray = []
	
	print("Original Array - " + str(array))

	for x in range(0, len(array)):
		reversedArray.append(array[(int(len(array)))-1 - x])

	print("Original Array - " + str(reversedArray))

# CALLING THE FUNCTIONS
# NOTE - In my previous programs, I included special loops and functions to catch errors or incorrect input. To make this program shorter, I will not be including them.
print("LESSON 2.1 - Pizza Shop\n--------------------\n")

print("Hello! Please enter your name - ")
name = input("")

print("\nWelcome to Dominos® Online Ordering System. How many pizzas will you order today?")
orderAmount = input("ANSWER - ")

print("\nNow please select your toppings. If you do not want any toppings, enter '0' for the number")	
peperroniAmount = input("PEPPERONI - ")

oliveAmount = input("\nOLIVES - ")

print("\nWould you also like to order a drink?\nIf so, please enter its name. If not, enter NONE.\n")
drinkOption = input("ANSWER - ")

lessonTwo_one (name, orderAmount, peperroniAmount, oliveAmount, drinkOption)

# --------
print("\n--------------------\nLESSON 2.2 - Average\n--------------------\n")

print("Please enter three numbers to find the average of.")

numberOne = int(input("NUMBER ONE - "))
numberTwo = int(input("NUMBER TWO - "))
numberThree = int(input("NUMBER THREE - "))

lessonTwo_two (numberOne, numberTwo, numberThree)

# --------
print("\n--------------------\nLESSON 4 - Dynamic Typing\n--------------------\n")
array = [0, 1, 2, 3]
lessonFour_one(array)

# --------
print("\n--------------------\nLESSON 5 - Conditionals + Booleans\n--------------------\n")
age = input("Enter your age - ")
lessonFive(age)

# --------
print("\n--------------------\nLESSON 7.1 - Word Array\n--------------------\n")
word = input("Enter a word (preferably relating to fast food) - ")

lessonSeven_one(word)

# --------
print("\n--------------------\nLESSON 7.2 - User Info\n--------------------\n")
name = input("Welcome to the Official NSA Data Collection Program! Please enter your full name - ")
color = input("\nNow enter your favorite color - ")
numberOfPets = input("\nFinally, please enter the number of pets you have - ")

lessonSeven_two(name, color, numberOfPets)

# --------
print("\n--------------------\nLESSON 7.3 - Bank Accounts\n--------------------\n")
code = input("Welcome to the CHASE® Online Banking System. Please enter the code of the account you wish to access - ")
lessonSeven_three(code)

# --------
print("\n--------------------\nLESSON 8.1 - Array Loop\n--------------------\n")
print("Hi! Please enter a word. This word will be added to the array. When you are done, please type in 'STOP'.")
word = input("WORD - ")
lessonEight_one(word)

# --------
print("\n--------------------\nLESSON 8.2 - Array Loop\n--------------------\n")
myArray = [0, 1, 2, 3, 4, 5, 6]
lessonEight_two(myArray)