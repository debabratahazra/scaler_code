import math


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = 5
    vol = (4 * math.pi * (A ** 3)) / 3
    vol_ceil = math.ceil(vol)
    print(vol_ceil)

    return 0


if __name__ == '__main__':
    main()
