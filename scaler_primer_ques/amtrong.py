def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    num = int(input())
    for i in range(1, num):
        num_str = str(i)
        sum = 0
        for j in num_str:
            sum += int(j) ** 3
        if sum == int(i):
            print(i)
    return 0


if __name__ == '__main__':
    main()
