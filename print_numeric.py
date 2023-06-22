def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    val = int(input())
    for i in range(1, val+1):
        init_val = 1
        for j in range(0, i):
            if j == i-1:
                print(init_val)
            else:
                print(init_val, end=' ')
            init_val += 1

    return 0


if __name__ == '__main__':
    main()
