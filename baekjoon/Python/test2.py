import sys
N = int(sys.stdin.readline())
k = 2
ans = 0
num = 0
cnt = 0
if N == 1:
    print(1)
else:
    while N>k:
        k = k*2
        cnt += 1
    num = 2**cnt
    while True:
        if num == N:
            break
        num += 1
        ans = ans+2
    print(ans)

