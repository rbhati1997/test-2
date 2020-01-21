"""
Question 55: Please write a program using generator to print the even numbers between 0 and n in
comma separated form while n is input by console.
"""
input_number = input("Write a number here: ")
lis1 = []
def generator(number):
	"""
	Generator function which prints even number.
	param:number
	yield:even number.
	"""	
	for x in range(number):
		if x%2==0:
			yield x

for x in generator(input_number):
	lis1.append(x)

print(str(lis1)[1:-1])
