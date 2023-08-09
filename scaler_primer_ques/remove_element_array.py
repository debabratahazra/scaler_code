# https://www.scaler.com/academy/mentee-dashboard/class/28672/assignment/problems/11456?navref=cl_tt_nv

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arr_size = int(input())
    arr_str = input()
    remove_index = int(input())
    arr_int = arr_str.split()
    # remove element from specified index
    arr_int.pop(remove_index-1)

    for i in arr_int:
        print(i, end=' ')

    return 0


if __name__ == '__main__':
    main()
