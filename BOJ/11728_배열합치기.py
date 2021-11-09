import sys
import heapq
input = lambda : sys.stdin.readline().strip()

na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = a+b
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr), end=' ')