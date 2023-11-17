def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input("Enter test cases number: "))
    all_total = []
    while test_case > 0:
        num = int(input("Enter number: "))
        # Add the digits and print
        total = 0
        while num > 0:
            reminder = num % 10
            total += reminder
            num //= 10
        all_total.append(total)

        test_case -= 1

    # print list values in each line
    print('\n'.join(str(element) for element in all_total))

    return 0


if __name__ == '__main__':
    main()
