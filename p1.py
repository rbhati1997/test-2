"""
Question 1: Write a program which will find all such numbers which are divisible by 7 but are not
a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in
a comma-separated sequence on a single line.
"""

#Printing result using start, stop, and step arguments in Python range() function.
lis = []
for x in range(2000,3200,7):
	if x % 5 != 0:
		lis.append(x)

print(lis)
