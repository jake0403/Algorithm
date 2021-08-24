import sys
import heapq

input = lambda : sys.stdin.readline().strip()

N = int(input())

q = []
classRoom = [list(map(int, input().split())) for _ in range(N)]
classRoom.sort()
heapq.heappush(q, classRoom[0][1])
cnt = 1
for i in range(1,N):
    if q[0] > classRoom[i][0]:
        heapq.heappush(q, classRoom[i][1])
        cnt+=1
    else:
        heapq.heappop(q)
        heapq.heappush(q, classRoom[i][1])

print(cnt)
# for i in range(N):
#     heapq.heappush(q,list(map(int, input().split())))
# classRoom = [0]*(q[-1][1]+1)
# for i in range(N):
#     s,e = heapq.heappop(q)
#     for i in range(s+1,e+1):
#         if classRoom[i]:
#             classRoom[i]+=1
#         else:
#             classRoom[i] = 1
# print(max(classRoom))