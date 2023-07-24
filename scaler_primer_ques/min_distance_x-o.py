import math

# https://www.scaler.com/academy/mentee-dashboard/class/7326/assignment/problems/10054/?navref=cl_pb_nv_tb


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    # Find the minimum distance between x-o in the entire array

    A = ['x', '.', '.', '.', 'o', '.', '.', '.', 'x', 'x', '.', '.',
         '.', 'o', '.', '.', '.', 'x,' '.', '.',
         '.', '.', '.', '.', '.', 'x', '.', '.', '.',
         'o', '.',  '.', '.', 'x', '.', '.', '.', 'o']

    last_x = -1
    last_o = -1
    ans = float('inf')

    for i in range(len(A)):
        if A[i] == 'x':
            last_x = i
            if last_o != -1:
                ans = min(ans, last_x - last_o)
        if A[i] == 'o':
            last_o = i
            if last_x != -1:
                ans = min(ans, last_o - last_x)
    if ans == float('inf'):
        ans = -1

    # minimum distance between x and o in array
    print(ans)

    return 0


if __name__ == '__main__':
    main()
