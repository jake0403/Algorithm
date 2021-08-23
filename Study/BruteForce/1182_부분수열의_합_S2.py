import sys
input = lambda : sys.stdin.readline().strip()

def dfs(idx, t):
    global cnt
    if idx >= N:
        return
    t += arr[idx]
    if t == S:
        cnt += 1
    dfs(idx+1, t - arr[idx])
    dfs(idx+1, t)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

dfs(0,0)
print(cnt)
