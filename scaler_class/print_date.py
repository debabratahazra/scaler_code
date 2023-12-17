'''
Q1
Create a date printing function
Should take in 4 arguments
day, month, year, style

styling logic:

style = 0: print in this format: d / m / y
style = 1: print in this format: m / d / y

style anything else: print "invalid style"

IMP: default style is 0


eg: print_date(d, m, y, s):

21, 7, 2023, 0
op: 21 / 7 / 2023
'''


def print_date(d, m, y, s=0):
    if s == 0:
        print(d, "/", m, "/", y)
    elif s == 1:
        print(m, "/", d, "/", y)
    else:
        print("invalid style")


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    print_date(21, 11, 2023)

    return 0


if __name__ == '__main__':
    main()
