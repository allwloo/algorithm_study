import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
B = list(map(int, sys.stdin.readline().split()))
B.sort(reverse=True)
sum = 0
for i in range(N):
    sum += A[i]*B[i]
print(sum)
