from os import system, name

def clear():
	_ = system('cls')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        return False

class Robot:
	# VARIABLES
	position = 0
	armPosition = 0
	inPosession = False
	score = 0

	#METHODS
	def move(self, x):
		self.position += x

		if self.position > 7 or self.position < 0 or is_number(x) == False:
			print("Could not move robot - you entered an invalid number.")
			self.position -= x
		else:
			print("The current position of the robot is now " + str(self.position) + ".")

	def arm(self, y):
		if y > 10 or y < 0 or is_number(y) == False:
			print("Could not raise arm - you entered an invalid number.")
		else:
			self.armPosition = y
			print("The arm is currently " + str(self.armPosition) + " inches off the ground.")

	def collectCube(self):
		if self.position != 2:
			print("Could not collect cube - robot must be in SQUARE 3 to collect a cube.")
		elif self.armPosition != 0:
			print("Could not collect cube - arm must be 0 INCHES off the ground to collect a cube.")
		elif self.inPosession != False:
			print("Could not collect cube - cube already in posession.")
		else:
			self.inPosession = True
			print("Robot is now in posession of the cube.")

	def scoreCube(self):
		if self.position != 7:
			print("Could not score cube - robot must be in SQUARE 7 to score a cube.")
		elif self.armPosition != 10:
			print("Could not score cube - arm must be 10 INCHES off the ground to collect a cube.")
		elif self.inPosession != True:
			print("Could not score cube - cube not in posession.")
		else:
			self.inPosession = False
			self.score += 5
			print("Robot has scored a cube. The score is now " + str(self.score) + " POINTS.")

# VARIABLES
robot = Robot()
continueProgram = True

# BODY
clear()
print("You have entered the ROBOT COMMAND TERMINAL. Control the robot with the following commands - \n M = MOVE\n A = MOVE ARM\n C = COLLECT CUBE\n S = SCORE")

while continueProgram == True:
	command = input("> ")

	while command != "M" and command != "A" and command != "C" and command != "S":
		print("That is not a valid command. Please try again.")
		command = input("> ")

	if command == "M":
		print("Enter number of spaces to move.")
		numberOfSpaces = input(">> ")

		robot.move(int(numberOfSpaces))

	elif command == "A":
		print("Enter number of inches to move the arm up or down. To move down, enter a negative number.")
		armNumberOfInches = input(">> ")

		robot.arm(int(armNumberOfInches))

	elif command == "C":
		robot.collectCube()

	elif command == "S":
		robot.scoreCube()

