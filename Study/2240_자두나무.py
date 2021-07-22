import sys

input = sys.stdin.readline

T, W = map(int, input().split())
plum_drop = [0]
for i in range(T):
    plum_drop.append(int(input()))

# 가만히 있을 때 == 0 그 후로 움직인 W 만큼 열 생성
# 0 ~ T+1 초 만큼 행으로 생성
dp = [[0]*(W+1) for _ in range(T+1)]
# 1초부터 T까지
for i in range(1, T+1):
    # 움직이지 않았을 때 누적해서 더함
    if plum_drop[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    # 움직일 수 있는 횟수 만큼 반복
    for j in range(1, W+1):

        # 자두(사람)은 1번 나무부터 시작하므로 j가 짝수일 때는 1번 나무에 있을 때
        if plum_drop[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        elif plum_drop[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))