from itertools import count


def isPrime(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False


print(isPrime(2147483647))
