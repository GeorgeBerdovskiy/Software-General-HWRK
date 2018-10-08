# CHALLENGE 1

for x in range(1000):
	if x % 3 == 0 or x % 5 == 0:
		print(str(x))

print("\n-------------\n")

# CHALLENGE 2

fibonicci = [1, 1]
evenFibonocci = []

for x in range(2, 100):
	newValue = int(fibonicci[x-2]) + int(fibonicci[x-1])

	if newValue <= 4000000:
		if newValue % 2 == 0:
			fibonicci.append(newValue)
			evenFibonocci.append(newValue)
			print(str(newValue))
		else:
			fibonicci.append(newValue)
	else:
		fibonicci.append(newValue)

sum = 0;

for x in range(0, len(evenFibonocci)):
	sum += evenFibonocci[x]

print("\nSUM - " + str(sum) + "\n-------------\n")

# CHALLENGE 3

largestPrime = 0

for x in range(1, 600851475143):
	if  600851475143 % x == 0:
		for y in range(1, x):
			if x % y == 0:
				if y == 1 or y == x:
					if x > largestPrime:
						largestPrime = x
						print(str(largestPrime))

# PLEASE NOTE - The way I did these challenges is the "brute force" way of doing it, so the program uses an enormous amount of memory and time to finish processing.
# There are better ways of doing it, but the lesson is about loops, and using loops is the easiest way to complete these challenges, so that is what I did.
