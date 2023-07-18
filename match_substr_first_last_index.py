# https://www.scaler.com/academy/mentee-dashboard/class/7326/assignment/problems/9961?navref=cl_tt_nv

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = ["a", "aa", "aab", "b", "bb", "bba", "bbb"]
    B = "bb"

    first_index = -1
    last_index = -1

    for i in range(len(A)):
        if A[i].startswith(B):
            if first_index == -1:
                first_index = i
            last_index = i

    C = [first_index, last_index]
    print(C)
    return 0


if __name__ == '__main__':
    main()
