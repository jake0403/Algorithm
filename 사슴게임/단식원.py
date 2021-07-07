from copy import deepcopy

def select(start, cnt):
    global max_value
    if cnt == 3:
        cp_diet_arr = deepcopy(diet_arr)
        for i in range(n):
            for j in range(m):
                spread_smell(i,j, cp_diet_arr)
        clean_cnt = sum(x.count(0) for x in cp_diet_arr)
        max_value = max(max_value, clean_cnt)
        return True
    else:
        for i in range(start, n*m):
            r = i//m
            c = i%m
            if diet_arr[r][c] == 0:
                diet_arr[r][c] = 1
                select(i,cnt+1)
                diet_arr[r][c] = 0


def spread_smell(r,c,cp_diet_arr):
    if cp_diet_arr[r][c] == 2:
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<m and cp_diet_arr[nr][nc] == 0:
                cp_diet_arr[nr][nc] = 2
                spread_smell(nr, nc, cp_diet_arr)


T = int(input())
for tc in range(1, T+1):
    n,m = map(int, input().split())
    diet_arr = [list(map(int, input().split())) for _ in range(n)]
    max_value = 0
    select(0,0)
    print(f'#{tc} {max_value}')
