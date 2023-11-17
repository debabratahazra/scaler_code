def calculateHcf(num1, num2):
    # Determine the smaller number
    smaller = min(num1, num2)

    # Find the HCF
    hcf = 1
    for i in range(smaller+1, 1, -1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            # first highest value is the HCF/GCD
            return i
    return hcf


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    values = []

    for test in range(test_case):
        a = int(input())
        b = int(input())
        hcf = calculateHcf(a, b)
        values.append(hcf)

    for i in range(test_case):
        print(values[i])

    return 0


if __name__ == '__main__':
    main()
