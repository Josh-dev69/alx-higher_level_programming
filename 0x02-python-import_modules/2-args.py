#!/usr/bin/python3

import sys

# get the number of arguments
num_args = len(sys.argv) - 1

# print the number of arguments and the list of arguments
if num_args == 0:
    print("0 arguments.")
else:
    if num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    
    # print the list of arguments
    for i in range(num_args):
        print("{}: {}".format(i+1, sys.argv[i+1]))
