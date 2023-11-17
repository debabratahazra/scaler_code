# https://www.scaler.com/academy/mentee-dashboard/class/142386/homework/problems/20825?navref=cl_tt_nv

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    n = int(input())
    for i in range(n):
        print("*", end="")
        for j in range(2, n):
            print(" ", end="")
        print("*")

    return 0


if __name__ == '__main__':
    main()
