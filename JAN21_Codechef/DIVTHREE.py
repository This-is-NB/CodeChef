for _ in range(int(input())):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    print("**", end="")
    print(min(sum(a)//k, d))
