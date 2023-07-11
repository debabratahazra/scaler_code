def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    input_str = []
    for i in range(test_case):
        input_str.append(input())
    for j in input_str:
        print(j[::-1])
    return 0


if __name__ == '__main__':
    main()
