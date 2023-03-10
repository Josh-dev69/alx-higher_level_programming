#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    no_of_args = len(sys.argv) - 1
    Sum_of_argv = 0

    for i in range(no_of_args):
        Sum_of_argv += int(sys.argv[i + 1])
    print("{}".format(Sum_of_argv))
