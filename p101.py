"""
Sort with lambda
A key function may also be created with the lambda expression.
It allows us to in-line function definition.
"""

L = [('Sam', 35),
    ('Max', 25),
    ('Bob', 30),
    ('Bob', 12)]
x = sorted(L, key=lambda x: (x[1],x[0]) )
print(x)	# [('Max', 25), ('Bob', 30), ('Sam', 35)]