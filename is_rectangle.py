def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = 5
    B = 2
    C = 2
    D = 5
    if A == B and C == D:
        print(1)
    elif A == C and B == D:
        print(1)
    elif A == D and B == C:
        print(1)
    else:
        print(0)

    return 0


if __name__ == '__main__':
    main()
