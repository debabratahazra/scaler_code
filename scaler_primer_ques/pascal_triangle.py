# https://www.scaler.com/academy/mentee-dashboard/class/28663/assignment/problems/68

def generate_pascals_triangle(rows):
    triangle = []

    for i in range(rows):
        # Each row starts and ends with 1
        row = [1]

        # Calculate the elements in the middle of the row
        for j in range(1, i):
            prev_row = triangle[i - 1]
            row.append(prev_row[j - 1] + prev_row[j])

        # Each row ends with 1
        if i > 0:
            row.append(1)

        for j in range(len(row), rows, 1):
            row.append(0)

        triangle.append(row)

    return triangle


def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row))


def main():

    A = 5

    pascals_triangle = generate_pascals_triangle(A)
    print_pascals_triangle(pascals_triangle)

    return 0


if __name__ == '__main__':
    main()
