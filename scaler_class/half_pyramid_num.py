""" 
For example if N = 4 then pattern will be like:

1 2 3 4
1 2 3
1 2
1 

"""


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    n = int(input())
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            if j == i:
                print(j, end="")
            else:
                print(j, end=" ")
        print()

    return 0


if __name__ == '__main__':
    main()
