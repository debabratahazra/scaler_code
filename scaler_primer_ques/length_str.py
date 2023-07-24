def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    test_case = int(input())
    length = []
    for i in range(test_case):
        strVal = input()
        length.append(len(strVal))
    for i in length:
        print(i)
    return 0


if __name__ == '__main__':
    main()
