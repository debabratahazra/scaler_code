def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    count = []
    for i in range(0, test_case):
        num = int(input())
        total = 0
        if num == 0:
            total += 1
        while num > 0:
            reminder = num % 10
            total += 1
            num = num // 10
        count.append(total)

    for val in count:
        print(val)

    return 0


if __name__ == '__main__':
    main()
