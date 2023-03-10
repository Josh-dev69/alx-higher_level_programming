#!/usr/bin/python3

if __name__ == "__main__":
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
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
