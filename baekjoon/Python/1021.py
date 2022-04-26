import sys
N, M = map(int, sys.stdin.readline().split())
M_list = list(map(int, sys.stdin.readline().split()))
index = 1
cnt = 0
print(M_list)
for i in range(M):
    while True:
        if index == M_list[i]:
            break
        else:
            if 
