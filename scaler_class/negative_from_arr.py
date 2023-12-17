def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arr = input()
    arr = arr.split()
    for i, v in enumerate(arr):
        if i == 0:
            continue
        v = int(v)
        if v < 0:
            print(v, end=" ")

    return 0


if __name__ == '__main__':
    main()
