def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    num = int(input())

    for i in range(1, num):
        total = getAdd(i)
        if total == i:
            print(total)

    return 0


def getAdd(num):
    total = 0

    while num > 0:
        reminder = num % 10
        total += (reminder ** 3)    # cube of the each digit
        num = num // 10

    return total


if __name__ == '__main__':
    main()
