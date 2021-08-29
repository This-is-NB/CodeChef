for _ in range(int(input())):
    n, m = input().split()
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    a.sort()
    b.sort()
    b.reverse()
    sw = 0
    i = 0
    while sum(a) < sum(b) and i < min(len(a), len(b)):
        temp = b[i]
        b[i] = a[i]
        a[i] = temp
        sw += 1
        i += 1
    if sum(a) < sum(b):
        print(-1)
    else:
        print(sw)
