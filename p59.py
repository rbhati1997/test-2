"""
Question 59:
Define a class Person and its two child classes: Male and Female. All classes have a method
"getGender" which can print "Male" for Male class and "Female" for Female class.
"""

#TUDO
class Person:
	"""
	Parent class of Male and Female class.
	"""
	@staticmethod
	def get_gender():
		Female.get_gender()
		Male.get_gender()

class Male(Person):
	"""
	Sub-class of Person.
	"""
	@staticmethod
	def get_gender():
		print("Male")

class Female(Person):
	"""
	Sub-class of Person.
	"""
	@staticmethod
	def get_gender():
		print("Female")

# Calling function of a class.
Person.get_gender()
