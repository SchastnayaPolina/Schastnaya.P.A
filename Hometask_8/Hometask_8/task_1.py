from math import sqrt


def isPrime(x):
    return all(x % i != 0 for i in range(2, int(sqrt(x) + 1)))


def isTwin(x):
    return isPrime(x) and (isPrime(x - 2) or isPrime(x + 2))


n = int(input())
print(*filter(isTwin, [x for x in range(n, 2 * n + 1)]))