def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    height = int(input())
    if height >= 195:
        print("abnormal")
    elif height >= 165 and height < 195:
        print("taller")
    elif height >= 150 and height < 165:
        print("average")
    else:
        print("dwarf")

    return 0


main()
