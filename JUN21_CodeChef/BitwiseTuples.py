# import math
# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     base = (2<<n-1) -1
#     print(int(math.pow(base,m)%1000000007))   
    
import math

def power(a, b):
     
    # Stores final answer
    ans = 1
    while(b>0):
        if(b&1):
            ans = (ans*a)%1000000007
        a = a*a%1000000007
        b = b>>1
    return ans

for t in range(int(input())):
    n,m = map(int,input().split())
    # base = (2<<n-1) - 1
    if n==1:
        print(1)
    else:
        base = power(2,n) -1
        print(power(base,m)%1000000007)   
    
    
