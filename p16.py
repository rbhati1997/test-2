"""
Question 16: Use a list comprehension to square each odd number in a list. The list is input by a
sequence of comma-separated numbers.
"""

#To get a number from console input.
numbers = input("Write numbers=")

def odd_num(numbers):
	"""
	Function to find and append odd number in a list.
	param:numbers
	"""
	lis = [i*i for i in numbers if i%2!=0]
	return lis
		
# Calling odd_num function.
odd_lis = odd_num(numbers)
print(str(odd_lis)[1:-1])
