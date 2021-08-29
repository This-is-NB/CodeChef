for i in range(int(input())):
    minturner =0
    n,k = map(int,input().split())
    chess = list(map(int,input().split()))
    c = sorted(chess)
    for j in c:
        if k%j == 0:
            minturner = j
    if minturner in c:
        print(minturner)
    else :
        print(-1)