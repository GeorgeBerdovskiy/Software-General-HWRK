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

code = input("Welcome to the CHASE® Online Banking System. Please enter the code of the account you wish to access - ")

while code not in bankAccounts:
	code = input("That is not a valid account code. Please try again - ")

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