def digit_to_name(num):
    if num == 0:
        return "zero"
    elif num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    else:
        return ""


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    value = int(input())
    name = []

    while value > 0:
        reminder = value % 10
        name.append(digit_to_name(reminder))
        value //= 10

    name.reverse()
    for n in name:
        print(n, end=" ")

    return 0


if __name__ == '__main__':
    main()
