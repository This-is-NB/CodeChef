def fact(n):
    if n<2:
        return 1
    else:
        return (n*fact(n-1))

for i in range(int(input())):
    n = int(input())
    print(fact (n))