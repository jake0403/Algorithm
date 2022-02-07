import sys
input = lambda : sys.stdin.readline().strip()

def dfs(depth):
    global total, rotate, visited
    if depth == N:
        calc = sum(abs(rotate[x] - rotate[x+1]) for x in range(N-1))
        total.append(calc)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        rotate.append(nums[i])
        dfs(depth+1)
        rotate.pop()
        visited[i] = 0


N = int(input())
nums = list(map(int, input().split()))
visited = [0]*N
total = []
rotate = []
dfs(0)
print(max(total))