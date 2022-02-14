import sys
input : lambda : sys.stdin.readline().strip()

def dfs(r, c, d):
    global total
    if len(d) == 6:
        if d not in total:
            total.append(d)
        return
    d += str(arr[r][c])
    for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr,nc, d)


arr = [list(map(int, input().split())) for _ in range(5)]
total = []
for i in range(5):
    for j in range(5):
        dfs(i,j,"")
print(len(total))