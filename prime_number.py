def is_prime(number):
    if number <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = int(input())
    if is_prime(A):
        print("Prime")
    else:
        print("Not prime")

    return 0


if __name__ == '__main__':
    main()
