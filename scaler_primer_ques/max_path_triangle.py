# https://www.scaler.com/academy/mentee-dashboard/class/7327/assignment/problems/11907

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = [
        [3, 0, 0, 0],
        [7, 4, 0, 0],
        [2, 4, 6, 0],
        [8, 5, 9, 3]
    ]

    triangle = A

    n = len(triangle)

    # Traverse the triangle from bottom to top
    for i in range(n - 2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # The maximum path sum will be stored at the top of the triangle
    print(triangle[0][0])

    return 0


if __name__ == '__main__':
    main()
