#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar = len(sys.argv) - 1
    arg = 'argument'
    if ar == 0:
        arg += 's.'
    elif ar > 1:
        arg += 's:'
    else:
        arg += ':'
    print("{:d} {}".format(ar, arg))
    if ar > 0:
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
