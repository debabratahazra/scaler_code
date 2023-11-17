def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    binary = input("Enter binary value: ")
    bin_val = int(binary)
    total = 0

    for i in range(0, len(binary), 1):
        reminder = bin_val % 10
        if reminder == 1:
            total += (2 ** i)
        bin_val = bin_val // 10

    print(total)
    return 0


if __name__ == '__main__':
    main()
