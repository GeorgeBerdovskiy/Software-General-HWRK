def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        return False

userinfo = []

name = input("Welcome to the Official NSA Data Collection Program! Please enter your full name - ")
userinfo.append(name)

color = input("\nNow enter your favorite color - ")
userinfo.append(color)

numberOfPets = input("\nFinally, please enter the number of pets you have - ")
while is_number(numberOfPets) == False:
		numberOfPets = input("That is not a valid number. Please try again - ")
userinfo.append(numberOfPets)

print("Thank you for complying with this required NSA Data Collection Program! Here is some of the data we collected -\n NAME - " + str(userinfo[0]) + "\n FAVORITE COLOR - " + str(userinfo[1]) + "\n NUMBER OF PETS - " + str(userinfo[2]))