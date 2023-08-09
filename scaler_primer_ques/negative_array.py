# https://www.scaler.com/academy/mentee-dashboard/class/28675/assignment/problems/11394

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arr_str = input()
    arr_int = arr_str.split()
    arr_size = arr_int[0]

    for val in arr_int:
        if int(val) < 0:
            print(val, end=' ')

    return 0


if __name__ == '__main__':
    main()
