import sys
N = []
M = 0
for i in range(int(sys.stdin.readline())):
    N.append(int(sys.stdin.readline()))
for i in range(max(N), 1, -1):
    bit = 0
    for j in range(0, len(N)-1):
        if N[j+1]%i != N[j]%i:
            break
        if j == len(N)-2:
            M = i
            bit = 1
            break
    if bit == 1:
        break
for i in range(2, M+1):
    if M % i == 0:
        print(i, end=' ')
    

