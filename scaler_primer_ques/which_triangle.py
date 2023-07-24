'''
If a==b==c, print equilateral,
if either a==b or b==c or c==a, print isosceles,
else print scalene.

https://www.scaler.com/academy/mentee-dashboard/class/28716/assignment/problems/11673/?navref=cl_pb_nv_tb
'''


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    get_input = input()  # Get input A B C in space separated
    substrings = get_input.split()
    A = float(substrings[0])
    B = float(substrings[1])
    C = float(substrings[2])
    if A == B and A == C:
        print("equilateral")
    elif A == B or A == C or B == C:
        print("isosceles")
    else:
        print("scalene")

    return 0


if __name__ == '__main__':
    main()
