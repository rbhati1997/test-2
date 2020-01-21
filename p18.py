"""
Question 18: A website requires the users to input username and password to register. Write a
program to check the validity of password input by users.
"""

import re

passwords = raw_input("Enter password to test: ")

def validation(passwords):
	"""
	Function to check validation for given passwords.
	param: passwords.
	"""
	password_list = passwords.split(",")

	# iteration password_list.
	for password in password_list:

		if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*[@#$])[A-Za-z\d@#$]{6,12}$', password):
			print(password)

# Calling validation function.
validation(passwords)
