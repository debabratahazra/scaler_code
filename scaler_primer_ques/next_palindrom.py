def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = "69459653"
    # A = '1740948824551711527614232216857618927954312334113874277931986502860248650900613893446066184963788291'
    while True:
        A = int(A) + 1
        if str(A) == str(A)[::-1]:
            print(A)
            return 0

    return 0


if __name__ == '__main__':
    main()
