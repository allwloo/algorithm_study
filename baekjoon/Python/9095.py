import sys
d = [0]*10005
d[1], d[2], d[3] = 1, 2, 4
for i in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    for j in range(4, k+1):
        d[j] = d[j-3] + d[j-2] + d[j-1]
    print(d[k]) 

