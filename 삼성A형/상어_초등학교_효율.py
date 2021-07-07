from collections import defaultdict
N = int(input())
arr = [[0]*N for _ in range(N)]
prefer_dic = defaultdict(list)
for _ in range(N**2):
    students = list(map(int, input().split()))
    prefer_dic[students[0]] = students[1:]

    maxR = 0
    maxC = 0

    maxP = -1
    maxZ = -1
    for r in range(N):
        for c in range(N):
            if not arr[r][c]:
                preCnt = 0
                zeroCnt = 0
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc] in students[1:]:
                            preCnt +=1
                        if arr[nr][nc] == 0:
                            zeroCnt+=1
                if maxP < preCnt or (maxP == preCnt and maxZ < zeroCnt):
                    maxR = r
                    maxC = c
                    maxP = preCnt
                    maxZ = zeroCnt
    arr[maxR][maxC] = students[0]

score = 0
score_table = {0:0, 1:1, 2:10, 3:100, 4:1000}
for r in range(N):
    for c in range(N):
        cnt = 0
        prefer = prefer_dic[arr[r][c]]
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] in prefer:
                    cnt+=1
        score += score_table[cnt]

print(score)