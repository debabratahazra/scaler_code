def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    T = int(input())
    strs = []
    for i in range(0, T):
        strs.append(input())
    for i in range(0, T):
        print(strs[i].replace(" ", ""))
    return 0


if __name__ == '__main__':
    main()
