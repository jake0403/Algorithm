from copy import deepcopy
from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
arr = [[0]*101 for _ in range(101)]
answer = 0

for _ in range(N):
    i,j = map(int, input().split())
    for r in range(i,i+10):
        for c in range(j, j+10):
            arr[r][c] = 1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+i, c+j
                if 0<=nr<101 and 0<=nc<101 and not arr[nr][nc]:
                    answer+=1
print(answer)