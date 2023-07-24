def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    rows = int(input())
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("* ", end="")
        print()
    for i in range(rows-1, -1, -1):
        for j in range(rows - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("* ", end="")
        print()

    return 0


if __name__ == '__main__':
    main()
