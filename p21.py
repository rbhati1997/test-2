import math
"""
Question 21 : A robot moves in a plane starting from the original point (0,0). The robot can move
toward UP, DOWN, LEFT and RIGHT with a given steps.
"""
UP = input("Write UP steps: ")
DOWN = input("Write DOWN steps: ")
LEFT = input("Write LEFT steps: ")
RIGHT = input("Write RIGHT steps: ")

def robot(UP,DOWN,LEFT,RIGHT):
	"""
	Print distance by given values.
	"""
	distance = math.sqrt(((UP-DOWN)**2) + ((LEFT-RIGHT)**2))
	print(int(round(distance)))

# Calling function.
robot(UP,DOWN,LEFT,RIGHT)
