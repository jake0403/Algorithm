from collections import deque
import sys
def DFS(sV, visited):
    visited+=[sV]
    for i in range(len(adj_arr[sV])):
        if adj_arr[sV][i] == 1 and i not in visited:
            DFS(i, visited)
    return visited

def BFS(sV):
    visited = [sV]
    Q = deque([sV])
    while Q:
        p = Q.popleft()
        for i in range(len(adj_arr[sV])):
            if adj_arr[p][i] == 1 and i not in visited:
                visited.append(i)
                Q.append(i)
    return visited

V , E, sV = map(int,sys.stdin.readline().split())
adj_arr = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e = map(int,sys.stdin.readline().split())
    # 무방향
    adj_arr[s][e] = 1
    adj_arr[e][s] = 1

print(*DFS(sV,[]))
print(*BFS(sV))
