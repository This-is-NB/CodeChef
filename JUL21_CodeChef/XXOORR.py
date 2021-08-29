import numpy as np
import math
# for _ in range(int(input())):
for _ in range(1):
    n,k = map(int,input().split())
    # print(n,k)
    # n,k = 3,2
    A = list(map(int,input().split()))
    # print(A)
    # A = [3,6,10]
    nbit = int(math.log(max(A),2) +1)
    
    res_list = np.zeros(nbit,dtype=np.uint16)
    for num in A:
        binary_rep = list("{0:b}".format(int(num)))
        for i in range(len(binary_rep)):
            res_list[-1-i] += int(binary_rep[-1-i])
        print(res_list) 
    ans =0
    for x in res_list:
        ans += math.ceil(x/k)
    print(ans)