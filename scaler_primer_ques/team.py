# https://www.scaler.com/academy/mentee-dashboard/class/28426/assignment/problems/4758/?navref=cl_pb_nv_tb

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = "001101"
    B = []
    for i in A:
        if i == "1":
            B.append("-1")
        else:
            B.append("1")
    # print(B)
    C = []
    for i in range(0, len(A), 1):
        if i == 0:
            C.append(int(B[0]))
        else:
            val = int(B[i]) + int(C[i-1])
            C.append(val)
    # print(C)
    count = 0
    for i in C:
        if i == 0:
            count += 1
    print(count)

    return 0


if __name__ == '__main__':
    main()
