# https://www.scaler.com/academy/mentee-dashboard/class/28660/assignment/problems/11381?navref=cl_tt_nv

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    test_case = int(input())
    A = []
    for i in range(0, test_case):
        number = int(input())

        total = 0
        while number > 0:
            digit = number % 10
            total += digit
            number //= 10
        A.append(total)

    for i in range(0, test_case):
        print(A[i])

    return 0


if __name__ == '__main__':
    main()
