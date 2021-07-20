import sys
import heapq

input = sys.stdin.readline

N = int(input())
pq = []

for i in range(N):
    num = list(map(int, input().split()))
    if pq:
        for n in num:
            if pq[0] < n:
                heapq.heappush(pq, n)
                heapq.heappop(pq)
    else:
        for n in num:
            heapq.heappush(pq, n)

print(pq[0])
