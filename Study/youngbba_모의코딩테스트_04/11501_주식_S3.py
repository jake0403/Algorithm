import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    ans = 0
    max_profit = stock[N-1]
    for i in range(N-2,-1,-1):
        if stock[i] > max_profit:
            max_profit = stock[i]
        else:
            ans += max_profit - stock[i]
    print(ans)

    min_profit = sys.maxsize
    profit = 0
    for s in stock:
        min_profit = min(min_profit, s)
        profit = max(profit, s - min_profit)
    print(profit)