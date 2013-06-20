import sys
import random


def main():
    # argv 0 is the script itself
    # just raise the ValueError if the values are wrong
    n = int(sys.argv[1])
    lo = float(sys.argv[2])
    hi = float(sys.argv[3])

    for i in range(n):
        print random.uniform(lo, hi)


if __name__ == "__main__":
    main()
