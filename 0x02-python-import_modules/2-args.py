#!/usr/bin/python3
if __name__ == "__main__":
    """
        Prints the number and list of arguments
    """
    import sys

    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("{} argument.".format(length))
    else:
        print("{} arguments.".format(length))

    for i in range(length):
        print("{}: {}".format(i, sys.argv[i + 1]))
