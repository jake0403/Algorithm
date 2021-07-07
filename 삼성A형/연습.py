from collections import deque
def bfs(m, m_list):
    global arr, ans, visited
    maxN = 0
    maxCnt = 2
    maxZ = 0
    maxR, maxC = 0, 0
    n = 1
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == m and not visited[r][c]:
                m_list.append([r,c])
                zcnt = 0
                visited[r][c] = n
                Q = deque()
                Q.append([r, c])
                cnt = 1
                flagR, flagC = r, c
                while Q:
                    r,c = Q.popleft()
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr = r + dr
                        nc = c + dc
                        if 0<= nr < N and 0<= nc <N:
                            if (arr[nr][nc] == m or arr[nr][nc] == 0) and not visited[nr][nc]:
                                cnt += 1
                                if arr[nr][nc] == 0:
                                    zcnt += 1
                                Q.append([nr, nc])
                                visited[nr][nc] = 1
                if maxCnt < cnt or (maxCnt == cnt and maxZ < zcnt) or (maxZ == zcnt and (maxR < flagR or maxC < flagC)):
                    maxCnt = cnt
                    maxZ = zcnt
                    maxR, maxC = flagR, flagC
                    maxN = n
                n += 1
    # 한개 밖에 없을 때
    if maxCnt == 1 and maxZ == 0:
        m_list.remove([r,c])
        return

    ans += maxCnt**2
    for i in range(maxR, N):
        for j in range(maxC, N):
            if visited[i][j] == maxN:
                arr[i][j] = -2
    arr = gravity(arr)
    m_list.remove([maxR,maxC])
    while m_list:
        bfs(m, m_list)



def gravity(arr):
    for r in range(N):
        for c in range(N-1):
            if arr[c][r] > 0 and arr[c+1][r] == -2:
                arr[c][r], arr[c+1][r] = arr[c+1][r], arr[c][r]
    print(f'arr : {arr}')
    g_arr = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            g_arr[N-1-c][r] = arr[r][c]
    print(g_arr)
    return g_arr

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0]*N for _ in range(N)]
for m in range(M, 0, -1):
    m_lst = []
    bfs(m, m_lst)

print(ans)