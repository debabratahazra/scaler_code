import math


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = 1332  # Squar_val
    edge = math.sqrt(A)
    print(edge)
    edge = round(edge, 1)
    sqrt_value = edge * edge
    print(sqrt_value)
    if A == sqrt_value:
        print(1)
    else:
        print(0)

    return 0


if __name__ == '__main__':
    main()
