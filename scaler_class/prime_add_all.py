import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primeSum(n):
    sum_of_primes = 0
    for i in range(n):
        if is_prime(i):
            sum_of_primes += i

    print(sum_of_primes)


def main():
    n = int(input())
    # for i in range(1, n+1):
    primeSum(n)


if __name__ == '__main__':
    main()
