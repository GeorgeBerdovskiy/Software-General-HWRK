class Animal:
	def __init__(self, fur, sweatGlands, diaphragm):
		self.hasFur = fur
		self.hasSweatGlands = sweatGlands
		self.hasDiaphragm = diaphragm

	def GetAnimalAttributes(self):
		return self.hasFur + self.hasSweatGlands + self.hasDiaphragm

class Mammal(Animal):
	def __init__(self, fur, sweatGlands, diaphragm):
		Animal.__init__(self, fur, sweatGlands, diaphragm)

	def GetMammalAttributes(self):
		return self.GetAnimalAttributes()

class Cat(Mammal):
	def __init__(self, fur, sweatGlands, diaphragm):
		Mammal.__init__(self, fur, sweatGlands, diaphragm)

	def GetAttributes(self):
		return self.GetMammalAttributes()

animal = Animal(False, False, False)
mammal = Mammal(True, True, True)
cat = Cat(True, True, True)

if int(cat.GetAttributes()) == 3:
	print("Cat has fur, sweat glands, and diaphragm.")
