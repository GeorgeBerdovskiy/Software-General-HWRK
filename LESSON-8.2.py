array = ["Zero", "One", "Two", "Three", "Four"]
reversedArray = []

print("Original Array - " + str(array))

for x in range(0, len(array)):
	reversedArray.append(array[(int(len(array)))-1 - x])

print("Original Array - " + str(reversedArray))