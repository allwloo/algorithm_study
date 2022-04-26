import sys
dp = [0]*10000
dp[1], dp[2] = 1, 2
k = int(sys.stdin.readline())
for i in range(3, k+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[k]%10007)