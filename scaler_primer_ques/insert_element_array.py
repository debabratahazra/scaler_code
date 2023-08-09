# https://www.scaler.com/academy/mentee-dashboard/class/28672/assignment/problems/11458

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arr_size = int(input())
    arr_str = input()
    insert_index = int(input())
    insert_element = int(input())
    arr_int = arr_str.split()
    # add element in specify index
    arr_int.insert(insert_index-1, insert_element)

    for i in arr_int:
        print(i, end=' ')

    return 0


if __name__ == '__main__':
    main()
