import sys

def dfs(r, c, time, eat):
    global max_eat
    if time == T:
        max_eat = max(max_eat, eat)
        return
    for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr,nc = r+dr, c+dc
        if 0<=nr<R and 0<=nc<C and arr[nr][nc] != '#':
            if arr[nr][nc] == 'S':
                arr[nr][nc] = '.'
                dfs(nr, nc, time+1, eat+1)
                arr[nr][nc] = 'S'
            else:
                dfs(nr,nc, time+1, eat)



def findG():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'G':
                return [i,j]


input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(input()) for _ in range(R)]
max_eat = 0
sr, sc = findG()
dfs(sr,sc,0,0)
print(max_eat)