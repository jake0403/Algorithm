def solution(n, computers):
    visited = [0]*n
    cnt = 0
    def dfs(node,cnt):
        visited[node] = 1
        for i in range(n):
            if not visited[i] and computers[node][i] == 1:
                cnt += 1
                visited[i] = 1
                dfs(i,cnt)
        return cnt
    answer = dfs(0,cnt)
    return n - answer

n = int(input())
computers = [list(map(int,input().split())) for _ in range(n)]

print(solution(n,computers))

'''
3
1 1 0
1 1 0
0 0 1

'''