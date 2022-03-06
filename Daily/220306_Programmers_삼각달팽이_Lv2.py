answer = []
n = 4
arr = [[-1] * n for _ in range(n)]
if n % 2 == 1:
    N = (n * n) // 2 + (n // 2 + 1)
else:
    N = (n * n) // 2 + n // 2

dr = [1, 0, -1]
dc = [0, 1, -1]
change = 0
r = c = 0
for i in range(1, N + 1):
    arr[r][c] = i
    nr = r + dr[change]
    nc = c + dc[change]
    # 범위를 넘어가지 않을 때
    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == -1:
        r, c = nr, nc
    else:
        if change == 2:
            change = 0
        else:
            change += 1
        nr = r + dr[change]
        nc = c + dc[change]
        r, c = nr, nc
for i in range(n):
    for j in range(n):
        if arr[i][j] != -1:
            answer.append(arr[i][j])
        else:
            break
print(answer)