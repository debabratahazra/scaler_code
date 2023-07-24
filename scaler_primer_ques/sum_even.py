def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = 10
    sum = 0
    for i in range(0, A+1, 2):
        sum += i
    print(sum)
    return 0


if __name__ == '__main__':
    main()
