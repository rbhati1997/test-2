"""
Question 54: Define a class named Shape and its subclass Square. The Square class has an init
function which takes a length as argument. Both classes have a area function which can print the
area of the shape where Shape's area is 0 by default.
"""
from abc import ABC, abstractmethod

class Shape(ABC):

	@abstractmethod
	def area(self):
		return 0

class Square(Shape):
	c_v = 10
	def __init__(self,length):
		self.length = length

	def area(self):
		print(self.c_v)
		print(self.length*self.length)

class_obj = Square(10)
class_obj.area()