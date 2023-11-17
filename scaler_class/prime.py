import math


def main():
    n = int(input())
    if n <= 1:
        print("False")
    elif n <= 3:
        print("True")
    elif n % 2 == 0 or n % 3 == 0:
        print("False")
    else:
        for i in range(5, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                print("False")
                return
        print("True")


if __name__ == '__main__':
    main()
