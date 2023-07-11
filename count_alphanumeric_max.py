def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = "Hello123World2"
    char_count = 0
    num_count = 0
    for ch in A:
        if ch.isalpha():
            char_count += 1
        elif ch.isdigit():
            num_count += 1
    if char_count > num_count:
        print(char_count)
    else:
        print(num_count)

    return 0


if __name__ == '__main__':
    main()
