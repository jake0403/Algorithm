import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for idx in range(coin, k+1):
        if idx - coin >= 0:
            dp[idx] += dp[idx-coin]
print(dp[k])