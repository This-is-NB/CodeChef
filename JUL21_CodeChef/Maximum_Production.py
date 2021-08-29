for i in range(int(input())):
    d,x,y,z = map(int,input().split())
    print(max(x*7, d*y + z*(7-d)))