import sys
import time
import math
N_list, M_list = [], ['7']*100000
N = int(sys.stdin.readline())
N_list = sys.stdin.readline().split()
N_list.sort()
M = int(sys.stdin.readline())
#M_list = sys.stdin.readline().split()
start = time.time()
for i in M_list:
    low = 0
    high = len(N_list)-1
    while True:
        k = math.floor((low+high)/2)
        if low > high:
            print(0)
            break
        if N_list[k] == i:
            print(1)
            break
        elif N_list[k] > i:
            high = k-1
        else:
            low = k+1
print("time :", time.time() - start)