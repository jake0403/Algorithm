'''
input
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

output
0
2
3
7
INF
'''

import heapq
import sys
input = lambda : sys.stdin.readline().strip()

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
