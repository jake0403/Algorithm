N, M = map(int, input().split())
num_list = [[0]*M for x in range(N)]
dr = [0, -1, 0, -1]
dc = [-1, 0, 1, 0]
row = N - 1
col = M -1
change = 0
num_list[row][col] = 1
for i in range(2,N*M+1):
    row += dr[change]
    col += dc[change]
    num_list[row][col] = i
    if change % 2 == 1:
        change += 1
        if change >= 3:
            change = 0
    nr = row + dr[change]
    nc = col + dc[change]
    if 0 <= nr < N and 0 <= nc < M and not num_list[nr][nc]:
        continue
    if change < 3:
        change+=1
    else:
        change  = 0

for i in num_list:
    print(*i)