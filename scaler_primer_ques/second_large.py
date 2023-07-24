def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    length = int(input())
    if length < 2:
        print("NA")
    arr = input()
    val_arr = arr.split(' ')
    arr_val = []
    for i in val_arr:
        arr_val.append(int(i))

    max_value = max(arr_val)
    second_largest = float('-inf')

    for num in arr_val:
        if num != max_value and num > second_largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("NA")
    else:
        print(second_largest)

    return 0


if __name__ == '__main__':
    main()
