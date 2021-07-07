def DFS(sV, eV, V): # s에서 g에 도착할 수 있는지 확인하는 함수
    # 중복없이 빠짐없이 탐색하는 dfs...
    stack = [] # 스택생성
    visited = [0]*(V+1) # 방문기록표 생성
    stack.append(sV) # push(s) 갈림길 목록에 시작점 추가
    while stack:       # 스택이 비어있지 않으면 (방문할 곳이 남아있으면)
        n = stack.pop() # 방문할 목록에서 마지막에 기록된 노드를 꺼내
        if visited[n]==0:
            visited[n] = 1
            if n==eV: # 방문한 노드가 목적지 g인지 확인
                return 1 # 경로가 존재
            for i in range(1, V+1): # 모든 노드에 대해, 현재노드에서 방문할 수 있는 곳인지 검토
                if adj_arr[n][i]==1 and visited[i]==0: # 인접하고 미방문인 노드 i를 찾으면
                    stack.append(i) # push(i)

    return 0 # 목적지에 도달하지 못하고, 탐색할 노드가 더이상 없는 경우

def BFS(sV):
    Q = [[sV, 0]]
    # 방문 체크를 위한
    visited = [False]*(V+1)
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)

        if v == eV:
            return dist
        for i in range(1,V+1):
            if adj_arr[v][i] == 1 and visited[i] == False:
                Q.append([i, dist+1])
                visited[i] = True
    return 0

def BFS2(sV):
    Q = [sV]
    visited = [False]* (V+1)
    visited[sV] = True

    dist = 0
    while Q:
        size = len(Q)
        # 거리에 따른 노드의 수만큼 반복
        for i in range(size):
            v = Q.pop(0)
            if v == eV: return dist

            for i in range(1,V+1):
                 if not visited[i] and adj_arr[v][i]:
                    Q.append(i)
                    visited[i] = True
        dist+=1
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())

    # 인접행렬을 이용하여 작성
    adj_arr = [[0]*V+1 for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        # 무방향이므로 양쪽 연결
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    sV , eV = map(int,input().split())
