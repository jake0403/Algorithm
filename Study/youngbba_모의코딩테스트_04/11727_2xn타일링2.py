import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
dp = [0, 1, 3, 5, 11]
for i in range(5,N+1):
    dp.append((dp[i-1]+ dp[i-2]*2) % 10007)
print(dp[N])