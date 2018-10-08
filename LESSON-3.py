# a. Are float(4.6) and int(4.6) the same? if not, how are they different.
# NO, they are NOT the same. This is because float(4.6) casts 4.6 to a float (decimal number), while int(4.6) casts 4.6 to an integer (whole number), "cuts off" the decimal WITHOUT rounding. Run the porgram and observe - 

x = float(4.6)
y = int(4.6)

print("PROBLEM A -\n")
print("Result of float(4.6) - " + str(x) + "\n")
print("Result of float(4.6) - " + str(y) + "\n\n")

# b. What does int(3.7) return?
# int(3.7) will return 3, because casting a decimal number to an integer will "cut off" the decimal without rounding. Run the program and observe -

z = int(3.7)

print("PROBLEM B -\n")
print("Result of int(3.7) - " + str(z) + "\n\n")

# c. Does int("4.5") work? Does int("4 and 5")?
# NO, int("4.5") does NOT work, because it ONLY converts the String to an integer, and if the contents of the String are NOT a valid integer, there will be an error. The correct way to do this would be to first convert the String into a float, and THEN convert that float into an integer.

#w = int("4.5")

#print("PROBLEM C - \n")
#print("Result of int(''4.5'') - " + str(w) + "\n\n")

# d. What happens when you try float("three point six")? Or float("three")?
# When you try these, the program will crash because when the String is converted into numerical characters, Python encounter letters instead of numbers, and it cannot assign a non-integer value to an integer.

#u = float("three point six")
#v = float("three")

#print("PROBLEM D - \n")
#print("Result of int(''three point six'') - " + str(u) + "\n\n")
#print("Result of int(''three'') - " + str(v) + "\n\n")