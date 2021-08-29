d = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h",
     8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p"}


def codetoalpha(a, b, c, d):
    return (int(a) + 2*int(b) + 4*int(c) + 8*int(d))


for _ in range(int(input())):
    n = int(input())
    s = list(input())
    s.reverse()
    for i in range(n//4):
        # print(s.pop(), s.pop(), s.pop(), s.pop())
        print(d[codetoalpha(s.pop(), s.pop(), s.pop(), s.pop())], end="")
    print()
