import sys
import math
M, N = map(int, sys.stdin.readline().split())
a = []
for i in range(M, N+1):
    bit = 0
    k = math.trunc(i)
    if i == 1:
        bit = 1
    if i == 2:
        a.append(i)
    else:
        for j in range(2, k):
            if i%j == 0:
                bit = 1
                break
        if bit == 0:
            print(i)
            a.append(i)