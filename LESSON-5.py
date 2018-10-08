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

age = input("Please enter your age (use a whole number) - ")

while is_number(age) != True:
	age = input("That is not a valid age please try again - ")

print("\nBased on your age, you are able to do the following - \n")

if int(age) >= 14:
	print(" JOIN ROBOTICS TEAM")
if int(age) >= 16:
	print(" DRIVE AND HAVE A JOB")
if int(age) >= 18:
	print(" ATTEND COLLEGE")
if int(age) >= 21:
	print(" BE AN ADULT")
if int(age) >= 35:
	print(" BECOME PRESIDENT")
elif int(age) < 14:
	print("Nothing from our list.")
else:
	# Print nothing. This "else" statement will never be called.
	print("")