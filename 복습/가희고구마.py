def dfs(gr, gc, t):
    global max_eat, time
    if t > time :
        return 0
    eat = 0
    if arr[gr][gc] == 'S':
        # 고구마일때 먹은 갯수 추가
        eat = 1
        # 먹은 처리
        arr[gr][gc] = '.'

    total = 0
    for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr, nc = gr+dr, gc+dc
        if 0<=nr<r and 0<=nc<c and arr[nr][nc] != '#':
            f = dfs(nr,nc, t+1)
            eat = max(eat, f)
    if total !=0:
        arr[gr][gc] = 'S'
    return total+eat

def findG(arr):
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'G':
                return [i,j]

import sys
input = sys.stdin.readline
r,c,time = map(int, input().split())
arr = [list(input()) for _ in range(r)]
max_eat = 0
# 가희 위치 찾기
sr, sc = findG(arr)
print(dfs(sr,sc,0))