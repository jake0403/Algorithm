'''
트리로 풀 필요 없음
'''

# def dfs(sn, arr):
#     if parent[sn] > 0:
#         arr.append(parent[sn])
#         dfs(parent[sn], arr)
#     return arr
# import sys
# input = sys.stdin.readline
# v = int(input())
# cn1, cn2 = map(int, input().split())
# e = int(input())
# parent = [0]*(v+1)
# cnt = 0
# for i in range(e):
#     p, c = map(int, input().split())
#     parent[c] = p
# cn1_lst = dfs(cn1, [])
# if cn2 in cn1_lst:
#     cnt = cn1_lst.index(cn2)+1
# else:
#     cn2_lst = dfs(cn2, [])
#     if len(cn1_lst) < len(cn2_lst):
#         cn1_lst, cn2_lst = cn2_lst, cn1_lst
#
#     for i in range(len(cn1_lst)):
#         for j in range(len(cn2_lst)):
#             if cn1_lst[i] == cn2_lst[j]:
#                 cnt = i+j+2
#                 break
#         if cnt: break
#     if not cnt:
#         cnt = -1
# print(cnt)
import sys
from collections import deque
def bfs(sv, ev):
    cnt = 0
    q = deque([(sv, cnt)])
    while q:
        v, cnt  = q.popleft()
        if v == ev:
            return cnt
        if not visited[v]:
            visited[v] = 1
            cnt+=1
            for n in adj[v]:
                if not visited[n]:
                    q.append([n, cnt])
    return -1


input = sys.stdin.readline
v= int(input())
sv, ev = map(int, input().split())
e = int(input())
adj = [[] for _ in range(v+1)]
visited = [0]*(v+1)
for i in range(e):
    p,c = map(int, input().split())
    adj[p] +=[c]
    adj[c] +=[p]
print(bfs(sv,ev))