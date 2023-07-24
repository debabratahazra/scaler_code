def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    min = float('inf')
    max = int(0)
    vals = input()
    val_arr = vals.split(' ')
    for i in range(1, len(val_arr)):
        if val_arr[i] == '':
            continue
        val = int(val_arr[i])
        if val < min:
            min = val
        if val > max:
            max = val
    print(str(max) + " " + str(min))

    return 0


if __name__ == '__main__':
    main()
