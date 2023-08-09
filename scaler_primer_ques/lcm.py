# https://www.scaler.com/academy/mentee-dashboard/class/28735/assignment/problems/11261
import math


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    A = []
    B = []
    C = []
    for i in range(0, test_case):
        A.append(int(input()))
        B.append(int(input()))
    for i in range(0, test_case):
        lcm = (A[i] * B[i]) // math.gcd(A[i], B[i])
        C.append(lcm)

    for val in C:
        print(val)

    return 0


if __name__ == '__main__':
    main()
