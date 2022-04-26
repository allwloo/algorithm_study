import sys
day = [0]*int(sys.stdin.readline())
T, P = [0]*len(day), [0]*len(day)
money = 0
for i in range(len(day)):
    T[i], P[i] = map(int, sys.stdin.readline().split())
print(T, P)
for i in range(0, len(day)):
    if i >= len(day):
        if day[i] != 1:
            for j in range(T[i]):
                day[i+j] = 1
            money += P[i]
print(money)


