words = ["Burger", "Pizza", "Hot Dog", "Corn Dog", "Chicken Nuggets", "French Fries", "Onion Rings", "Fried Chicken", "Sandwich", "Soda"]

word = input("Enter a word (preferably relating to fast food) - ")

if word in words:
	print("\nThis word already exists.")
else:
	words.append(word)
	print("\n'" + word + "' has been added to the array. Here is the full array - ")
	print(words)