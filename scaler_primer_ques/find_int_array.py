def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    test_case = int(input())
    for i in range(0, test_case):
        arr_len = int(input())
        arr = input()
        val_arr = arr.split(' ')
        search = int(input())
        found = False
        for j in range(0, arr_len):
            if search == int(val_arr[j]):
                found = True
                print(1)
                break
        if not found:
            print(0)

    return 0


if __name__ == '__main__':
    main()
