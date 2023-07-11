def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    no_of_row = int(input())
    for i in range(1, no_of_row+1):
        for j in range(0, i):
            print("*", end='')
        print("\n", end='')
    return 0


if __name__ == '__main__':
    main()
