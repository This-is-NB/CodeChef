w, bal = map(float,input().split())
if w%5 == 0 and bal - w >=0.50:
    bal = bal -w - 0.50
print ("{0:.2f}".format(bal))
