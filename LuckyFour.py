# def count(a):
#     d={}
#     for i in a:
#         d[i] = d.get(i,0)+1
#     return d[4]

# for i in range(int(input())):
#     a = (map(int, list(input())))
#     if 4 in a:
#         print(count(a))
#     else:
#         print(0)
from collections import Counter
for i in range(int(input())):
    a = Counter(map(int, list(input())))
    if 4 in a:
        print(a[4])
    else:
        print(0)    