import sys
input = sys.stdin.readline

N, K = map(int, input().split())
w_list = []
v_list = []
for _ in range(N):
    w,v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

'''
# W: 배낭 무게 한도
# wt: 물건 무게
# val : 물건 가치
# n : 물건 수
'''
def knapsack(W, wt, val, n):
    dp = [[0]*(W+1) for _ in range(n+1)]

    # 물건 개수 만큼 돌면서
    for i in range(n+1):
        # 무게
        for w in range(W+1):
            if i == 0 or w ==0 : dp[i][w] =0
            elif wt[i-1] <= w:
               dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

ans = knapsack(K, w_list, v_list, N)
