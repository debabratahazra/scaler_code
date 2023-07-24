def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = "Hello"
    B = ""
    for i in A:
        val = ord(i)
        if val >= 65 and val <= 90:
            char = val + 32
            # print(chr(char), end='')
            B += chr(char)
        if val >= 97 and val <= 122:
            char = val - 32
            # print(chr(char), end='')
            B += chr(char)
    print(B)
    return 0


if __name__ == '__main__':
    main()
