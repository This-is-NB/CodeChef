try:
    def check(c):
        b1 = [c.pop()]
        b2 = [c.pop()]
        while(len(c) > 0):
            if (sum(b1) <= sum(b2)):
                b1.append(c.pop())
            else:
                b2.append(c.pop())
        print(max(sum(b1), sum(b2)))

    for _ in range(int(input())):
        n = int(input())
        c = list(map(int, input().split()))
        c.sort()
        check(c)
except:
    pass
