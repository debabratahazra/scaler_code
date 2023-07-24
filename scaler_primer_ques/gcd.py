# https://www.scaler.com/academy/mentee-dashboard/class/28658/assignment/problems/269

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = 4
    B = 6

    while B != 0:
        A, B = B, A % B
    print(A)
    return 0


if __name__ == '__main__':
    main()
