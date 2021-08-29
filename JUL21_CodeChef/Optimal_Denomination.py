from collections import namedtuple
import math

def gcd(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        temp = math.gcd(temp,arr[i])
    return temp


for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    if n == 1: 
        print(1)
        continue
    if len(set(A)) == 1: 
        print(len(A))
        continue
    max_gcd = 0
    for ele in sorted(A):
        temp = A.copy()
        temp.remove(ele)
        g = gcd(temp)
        # print (temp ,g)
        if g >= max_gcd:
            max_gcd = g
            final = temp
    ans = [ ele//max_gcd for ele in final]
    # print(ans, max_gcd)
    print( sum(ans) + 1)
    
# if __name__="__main__":
    # print(main())
    # print()