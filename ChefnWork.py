for i in range(int(input())):
    n,k = map(int,input().split())
    w = list(map(int,input().split()))
    w.reverse()
    temp =[]
    rounds = 0
    while len(w)!= 0:
        if w[-1] <= k :
            temp.append(w[-1])
            t=w.pop()
        else:
            print(-1)
            break
        if sum(temp) > k:
            temp =[]
            w.append(t)
            rounds += 1
        elif sum(temp) ==k:
            temp =[]
            rounds += 1
        elif len(w)==0 and sum(temp) <k:
            rounds += 1
        
    if rounds !=0:
        print(rounds)
                        