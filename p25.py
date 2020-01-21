"""
Question 25:
Define a class, which have a class parameter and have a same instance parameter.
"""
input_name = raw_input("Write your name: ")

class param(object):
	"""
	class have parameter and a same instance parameter.
	"""

	def __init__(self, name):
		self.name = name


person = param(input_name)
print(person.name)