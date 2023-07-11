def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    val = int(input())
    for i in range(val, 0, -1):
        if i == val:
            for j in range(0, i):
                print("*", end='')
            print(end='\n')
        else:
            for j in range(0, i):
                if j == 0 or j == i-1:
                    print("*", end='')
                else:
                    print(" ", end='')
            print(end='\n')

    return 0


if __name__ == '__main__':
    main()
