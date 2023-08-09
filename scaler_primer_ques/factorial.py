def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    n = int(input())
    factorial = 1
    for j in range(1, n+1, 1):
        factorial = factorial * j
    print(factorial)
    return 0


if __name__ == '__main__':
    main()
