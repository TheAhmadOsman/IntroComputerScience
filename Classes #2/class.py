class Rectangle:
	#Rectangle class for working with rectangles

	def __init__(self, width = 1, height = 1):
		self.width = width
		self.height = height

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def setWidth(self, width):
		self.width = width

	def setHeight(self, height):
		self.height = height

	def calcArea(self):
		return self.width * self.height

	def calcPeri(self):
		return (self.width + self.height) * 2

	def __str__(self):
		displayStr = "Width: " + str(self.width) + "\n" + "Height: " + str(self.height)
		return displayStr

def main():
	#Create three instances of a rectangle objec
	rect1 = Rectangle()
	print(rect1)

	rect2 = Rectangle(4, 8)
	print(rect2)
	print(rect2.calcArea())
	print(rect2.calcPeri())

	rect3= Rectangle(5)
	print(rect3)

main()