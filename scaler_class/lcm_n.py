# Formula:::::::::  LCM(a, b) = (a * b) / GCD(a, b)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def calculateLCM(a, b):
    return (a * b) // gcd(a, b)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    values = []

    for test in range(test_case):
        a = int(input())
        b = int(input())
        lcm = calculateLCM(a, b)
        values.append(lcm)

    for i in range(test_case):
        print(values[i])

    return 0


if __name__ == '__main__':
    main()
