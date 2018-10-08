from os import system, name

def clear():
    # Windows
    if name == 'nt': 
        _ = system('cls') 
    # Mac and Linux
    else: 
        _ = system('clear') 

clear()

print("Welcome to Math® Average Calculator. Please enter the three INTEGERS you wish to find the average of.\n")
# PLEASE NOTE - In order to satisfy the requirments of the challenge, I used int(input("")) to collect an INTEGER value from the user. If the user enters something that is not an integer, the program will crash. This is what I would write instead.

'''
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

numberOne = input("NUMBER ONE - ")

while is_number(numberOne) != True:
    print("\nThat is not a valid integer. Please try again.")
    numberOne = input("NUMBER ONE - ")

numberTwo = input("NUMBER TWO - ")

while is_number(numberTwo) != True:
    print("\nThat is not a valid integer. Please try again.")
    numberTwo = input("NUMBER TWO - ")

numberThree = input("NUMBER THREE - ")

while is_number(numberThree) != True:
    print("\nThat is not a valid integer. Please try again.")
    numberThree = input("NUMBER THREE - ")

average = (int(numberOne) + int(numberTwo) + int(numberThree)) / 3

'''

numberOne = int(input("NUMBER ONE - "))
numberTwo = int(input("NUMBER TWO - "))
numberThree = int(input("NUMBER THREE - "))

average = (numberOne + numberTwo + numberThree) / 3

print("\nThe average of " + str(numberOne) + ", " + str(numberTwo) + ", and " + str(numberThree) + " is " + str(average) + ".")