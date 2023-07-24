def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    nth_element = int(input())

    if nth_element == 0:
        print(0)
        return 0
    previous_sum = 0
    if nth_element == 1:
        print(1)
        return 0
    current_val = 1

    for i in range(2, nth_element + 1, 1):
        current_X = previous_sum + current_val
        previous_sum = current_val
        current_val = current_X
    print(current_val)

    return 0


if __name__ == '__main__':
    main()
