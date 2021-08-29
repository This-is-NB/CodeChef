import math


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


P = [i for i in range(1e6) if (is_prime(i))]


for _ in range(int(input())):
    a = []
    n = int(input())
    b = list(map(int, input().split()))
    for i in range(n):
        a.append(P[b[i] - 1])
    print(a)
