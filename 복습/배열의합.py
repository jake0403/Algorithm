def dfs(total, visited, arr, r):
    global min_sum
    if total >= min_sum:
        return
    if r==n and min_sum > total:
        min_sum = total
    else:
        for c in range(n):
            if not visited[c]:
                visited[c] = 1
                total+=arr[r][c]
                dfs(total, visited, arr, r+1)
                visited[c] = 0
                total-=arr[r][c]


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    visited = [0]*n
    arr = [list(map(int,input().split())) for _ in range(n)]
    min_sum = 99
    dfs(0, visited, arr, 0)
    print(f'#{tc} {min_sum}')