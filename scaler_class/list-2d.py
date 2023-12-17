'''
Take a 3X3 matrix as an input from the user. Given this matrix.
Calculate the sum of all the elements in the matrix.
Calculate the sum of each row
Calculate the sum of each column.
'''


def main():

    matrix = []
    # insert element in matrix
    print("Enter the 3x3 matrix values::")
    for i in range(3):
        row = []
        for j in range(3):
            value = int(input())
            row.append(value)
        matrix.append(row)

    # print the matrix
    print("Matrix value::")
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

    # calculate the matrix sum
    sum = 0
    for row in matrix:
        for elem in row:
            sum += elem
    print("Total sum: ", sum)

    # calculate the matrix row wise
    sum = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            sum[i] += matrix[i][j]
    print("Total row wise sum:", sum)

    # calculate the sum of column wise
    sum = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            sum[j] += matrix[i][j]
    print("Total column wise sum:", sum)

    return 0


if __name__ == '__main__':
    main()
