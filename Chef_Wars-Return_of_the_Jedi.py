def check(h,p):
    hlth = h- p
    if hlth <= 0:
        return 1
    elif p == 0:
        return 0 
    else:
        return check(hlth,p//2)
    
for i in range(int(input())):
    h,p = map(int,input().split())
    print(check(h,p))