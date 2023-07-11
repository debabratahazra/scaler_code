def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    B = 2
    C = []
    for i in range(0, len(A)):
        C.append(A[i] + B)
    print(C)

    return 0


if __name__ == '__main__':
    main()
