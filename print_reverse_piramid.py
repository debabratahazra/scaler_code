def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    val = int(input())
    for i in range(val, 0, -1):

        for j in range(0, i):
            if j == i-1:
                print("*")
            else:
                print("*", end='')

    return 0


if __name__ == '__main__':
    main()
