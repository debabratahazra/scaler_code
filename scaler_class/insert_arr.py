def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    length = int(input())
    arr = input()
    arr = arr.split()
    position = int(input())
    val = int(input())

    arr.insert(position-1, val)

    for i in arr:
        print(i, end=" ")

    return 0


if __name__ == '__main__':
    main()
