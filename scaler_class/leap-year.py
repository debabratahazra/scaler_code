def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    year = int(input())
    if year % 100 == 0:
        if year % 400 == 0:
            print(1)
            return 1
        else:
            print(0)
            return 0
    else:
        if year % 4 == 0:
            print(1)
            return 1
        else:
            print(0)
            return 0

    return 0


if __name__ == '__main__':
    main()
