"""
Question 62: Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and
how many chickens do we have?
"""

num_heads=input("Write number of heads: ")
num_legs=input("Write number of legs:")

hens = 0
rabbit = 0

def puzzle(num_heads,num_legs):
	"""
	Find how many rabbits and chickens do we have.
	param:num_heads, num_legs
	return:number of rabbit and hens.
	"""
	rabbit = int((num_legs - (2*num_heads))/2)
	hens   = int(num_heads - rabbit)
	return rabbit,hens

# Calling funtion.
rabbit,hens=puzzle(num_heads,num_legs)
print ("rabbit=", rabbit)
print("hens= ", hens)

