"""
Sort with Operator Module Functions
To access items of an iterable,
Python provides convenience functions like itemgetter() and attrgetter() from operator module.
"""

from operator import itemgetter

L = [('Sam', 35),
    ('Max', 25),
    ('Bob', 30),
    ('Bob', 12)]
x = sorted(L, key=itemgetter(0,1))
print(x)	# [('Max', 25), ('Bob', 30), ('Sam', 35)]