import sys
input = lambda : sys.stdin.readline().strip()

def dfs(ans, idx):
    if len(ans) == C:
        print(" ".join(map(str, ans)))
        return
    for i in range(idx, N+1):
        if i not in ans:
            ans.append(i)
            dfs(ans,i)
            ans.pop()
N, C = map(int, input().split())
dfs([],1)