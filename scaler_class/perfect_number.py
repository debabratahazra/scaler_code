""" 
Given the Number of Test Cases as T,
For each test case, take an integer N as input, you have to tell whether it is a perfect number or not.

A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself). 
A positive proper divisor divides a number without leaving any remainder. 

6, the answer is "YES" as sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6.

"""


def checkPerfectNumber(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return "YES"
    else:
        return "NO"


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    values = []

    for i in range(test_case):
        values.append(int(input()))

    for val in values:
        ret = checkPerfectNumber(val)
        print(ret)

    return 0


if __name__ == '__main__':
    main()
