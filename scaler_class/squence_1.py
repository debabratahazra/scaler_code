# Using a loop, Print the squares of the following numbers: 1, 3, 6, 10, 15, 21. Print each of the number in a new line.

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    num = 1
    gap = 2

    for i in range(6):
        print(num)
        num += gap
        gap += 1

    return 0


if __name__ == '__main__':
    main()
