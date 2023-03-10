#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

# Perform addition
add_result = add(a, b)

# Perform subtraction
sub_result = sub(a, b)

# Perform multiplication
mul_result = mul(a, b)

# Perform division
div_result = div(a, b)

# Printing the Results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
