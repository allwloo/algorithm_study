import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
M_list = [0]*1005
M_list[0] = N_list[0]
for i in range(1, N):
    M_list[i] = N_list[i] + M_list[i-1]
print(sum(M_list))
