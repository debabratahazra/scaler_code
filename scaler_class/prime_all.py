import math


def primeCheck(n):
    if n <= 1:
        pass
    elif n <= 3 and n > 1:
        print(n)
    elif n % 2 == 0 or n % 3 == 0:
        pass
    else:
        for i in range(5, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                pass
                return
        print(n)


def main():
    n = int(input())
    for i in range(1, n+1):
        primeCheck(i)


if __name__ == '__main__':
    main()
