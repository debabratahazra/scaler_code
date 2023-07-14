import math


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    '''
    Rounded value of 2.4 = 2
    Rounded value of 2.5 = 3
    Rounded value of 2.6 = 3
    Rounded value of 0.0 = 0
    Rounded value of - 2.4 = -2
    Rounded value of - 2.5 = -3
    Rounded value of - 2.6 = -3
    '''

    A = -4.495
    decimal, integer = math.modf(A)
    decimal = round(decimal, 3)
    print(decimal)
    print(integer)
    print(A)
    if decimal >= 0.5 and A >= 0:
        # +ve more
        A = int(integer+1)
        print(A)
    elif decimal >= -0.499 and A < 0:
        # -ve more
        A = int(integer)
        print(A)
    elif decimal < 0.5 and A >= 0:
        # +ve less
        A = int(integer)
        print(A)
    elif decimal <= -0.5 and A < 0:
        # -ve less
        A = int(integer-1)
        print(A)

    return 0


if __name__ == '__main__':
    main()
