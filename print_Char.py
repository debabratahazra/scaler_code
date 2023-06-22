def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    ascii_A = 65
    val = int(input())
    for i in range(1, val+1):
        for j in range(0, i):
            if j == i-1:
                print(chr(ascii_A))
            else:
                print(chr(ascii_A), end=' ')
        ascii_A += 1

    return 0


if __name__ == '__main__':
    main()
