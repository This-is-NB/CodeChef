S = []
T = []
maxleadS =0
maxleadT =0
maxlead = [[],[]]
for _ in range (int(input())):
    s,t = input().split()
    S.append(s)
    T.append(t)
    lead=sum(S)-sum(T)
    if (lead >=0):
        maxlead[0].append(lead)
    else :
        maxlead[1].append(lead)
    
        