def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    for i in range(test_case):
        # input
        arr_size = int(input())
        arr_str = input()
        val_arr = arr_str.split(' ')
        find_val = input()
        if find_val in val_arr:
            print(1)
        else:
            print(0)
    return 0


if __name__ == '__main__':
    main()
