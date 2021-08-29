for i in range(int(input())):
    D,d,P,Q= map(int,input().split())
    if D%d == 0:
        DwQ = D-d # days with Q
        n = DwQ//d # perfect intervals of Q
        inc = (n*(n+1)//2)*Q*d # increment after each interval
        ans = P*D + inc 
    else:
        DwQ = D-d # days with Q
        n = DwQ//d # perfect intervals of Q
        inc = (n*(n+1)//2)*Q*d # increment after each interval
        extra = (D%d)*(n+1)*Q
        ans = P*D + inc + extra
    # if D&1 == 1:
    #     ans -= intervals*Q
    print(ans)
    
    # inc = 0
    # ans = 0
    # for i in range(1,D+1):
    #     ans += P+inc
        