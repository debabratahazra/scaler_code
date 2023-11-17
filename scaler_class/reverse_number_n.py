def reversed(value):
    sum = 0
    while value != 0:
        last = value % 10
        sum = (sum * 10)+last
        value = value//10
    return sum


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    test_case = int(input())
    values = []

    for i in range(test_case):
        val = int(input())
        values.append(val)

    for i in range(test_case):
        val = values[i]
        values[i] = reversed(val)

    for i in range(test_case):
        print(values[i])

    return 0


if __name__ == '__main__':
    main()
