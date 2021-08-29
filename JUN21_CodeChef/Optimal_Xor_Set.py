import math

def invertBits(num):
    x = int(math.log(num, 2.0) + 1) 
    for i in range(0, x):
        num = (num ^ (1 << i));
    
    return num ;


def optimal_xor_set(n,k):
    if k ==1:return [n]
    if k ==2:return [n,invertBits(n)]
    return -1

for i in range(int(input())):
    n,k = map(int,input().split())
    ans = optimal_xor_set(n,k)
    print(*ans)