for i in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    d = {}
    
    time = 0
    flag = False
    i = 1
    for ele in a:
        temp = []
        if ele == 1:
            flag = True
            time = 0
            
        if flag:
            temp.append(time)
            time += 1
        
        d[i] = d.get(i,[]) + temp
        i+=1 
        
   
    time = 0
    flag = False
    i = n
    for ele in reversed(a):
        temp = []
        if ele == 2:
            flag = True
            time = 0
            
        if flag:
            temp.append(time)
            time += 1
        
        d[i] = d.get(i,[]) + temp
        i-=1    
    d[1] = [0]
    print(d)
    for city in b:
        if len(d[city])>0:
            print(min(d[city]), end = " ")
        else:
            print(-1 , end=" ")
    print("\n")
    
            
             
            