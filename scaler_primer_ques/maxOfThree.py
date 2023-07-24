def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    a = int(input())
    b = int(input())
    c = int(input())
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    elif c >= a and c >= b:
        print(c)

    return 0


if __name__ == '__main__':
    main()
