"""
Question 19: You are required to write a program to sort the (name, age, height) tuples by
ascending order where name is string, age and height are numbers.
"""

#Sort with Operator Module Functions(itemgetter)
from operator import itemgetter
persons = []

while True:
	line = raw_input("> ")
	if not line:
		break
	persons.append(tuple(line.split(',')))
# Sort using itemgetter.
print(sorted(persons, key=itemgetter(0,1,2)))


"""
OR 
"""

# SORT USING LAMBDA FUNTION.
# persons = []
# while True:
# 	line = raw_input("> ")
# 	if not line:
# 		break
# 	persons.append(tuple(line.split(',')))
# # Sort using itemgetter.
# print(sorted(persons, key=lambda x: (x[0],x[1],x[2])))
