def isDivisible(x, y):
	if int(x) % int(y) == 0:
		return True
	else:
		return False

print("Please enter two numbers...\n")
x = input("NUMBER ONE - ")
y = input("NUMBER TWO - ")

if isDivisible(x, y) == True:
	print(x + " is divisible by " + y + ".")
else:
	print(x + " is NOT divisible by " + y + ".")