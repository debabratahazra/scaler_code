# https://www.scaler.com/academy/mentee-dashboard/class/28680/assignment/problems/11616

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    C = []

    rows = len(A)
    columns = len(A[0])

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    for row_val in C:
        print(row_val)

    return 0


if __name__ == '__main__':
    main()
