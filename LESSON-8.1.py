from os import system, name

def clear():
	# Windows
    if name == 'nt': 
        _ = system('cls') 

    # Mac and Linux
    else: 
        _ = system('clear') 

array = []
clear()

print("Hi! Please enter a word. This word will be added to the array. When you are done, please type in 'STOP'.")
word = input("WORD - ")

while word != "STOP":
	array.append(word)

	print("\nThat word has been added to the array. Please enter another word.")
	word = input("WORD - ")

print("\nYou have selected 'STOP'. Here is the array we created - ")
print(str(array))
