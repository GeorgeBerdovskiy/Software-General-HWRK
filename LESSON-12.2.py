from math import sqrt

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

for i in range(len(numbers)):
	number = numbers[i]
	print("Square root of " + str(number) + " is " + str(sqrt(number)))