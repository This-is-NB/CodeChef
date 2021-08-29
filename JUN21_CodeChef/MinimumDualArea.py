
inf = float("inf")

for _ in range(int(input())):
    minX = {}
    maxX = {}
    minY = {}
    maxY = {}
    
    n = int(input())
    for i in range(n):
        x,y = map(int,input().split())
        
        minY[x] = min(minY.get(x,inf),y)
        maxY[x] = max(maxY.get(x,-inf),y)
        minX[y] = min(minX.get(y,inf),x)
        maxX[y] = max(maxX.get(y,-inf),x)
    
    X = sorted(list(minY.keys()))
    Y = sorted(list(minX.keys()))
    print(X,Y)
    area = inf
    
    rect_from_start, rect_from_end = [],[]
    top,bottom = -inf,inf
    for x in X:
        top = max(top,maxY[x])
        bottom = min(bottom, minY[x])
        rect_from_start.append((x-X[0])*(top-bottom))
                
    top,bottom = -inf,inf
    for x in X[::-1]:
        top = max(top,maxY[x])
        bottom = min(bottom, minY[x])
        rect_from_end.append((X[-1]-x)*(top-bottom))
    rect_from_end.reverse()
    # print(rect_from_end ,"\n", rect_from_start)
    rect_from_end.append(0)
    for i in range(len(X)):
        area = min(area,rect_from_end[i+1]+rect_from_start[i])      
    
    rect_from_start, rect_from_end = [],[]
    top,bottom = -inf,inf
    for y in Y:
        top = max(top,maxX[y])
        bottom = min(bottom, minX[y])
        rect_from_start.append((y-Y[0])*(top-bottom))
                
    top,bottom = -inf,inf
    for y in Y[::-1]:
        top = max(top,maxX[y])
        bottom = min(bottom, minX[y])
        rect_from_end.append((Y[-1]-y)*(top-bottom))
    rect_from_end.reverse()
    rect_from_end.append(0)
    # print(rect_from_end ,"\n",rect_from_start)
    for i in range(len(Y)):
        area = min(area,rect_from_end[i+1]+rect_from_start[i])  
    print(area)
    # print(minX,"\n" ,maxX,"\n" ,minY,"\n" ,maxY,"\n" ) 
    # area(XwrtY)
    
    
