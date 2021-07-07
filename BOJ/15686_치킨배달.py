import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최적화된 짧은 거리 구하기
def find_shortest(L):
    shortest = sys.maxsize
    for i in range(len(res)):
        dist = 0
        for l in L:
            temp = sys.maxsize
            for j in range(M):
                temp = min(temp, abs(l[0] - res[i][j][0]) + abs(l[1] - res[i][j][1]))
            dist+= temp
        shortest = min(shortest, dist)

    return shortest

# 집 위치 구하기
def house():
    location = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                location.append([i,j])
    return location

chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i,j])
# M 개의 가게 조합 구하기
res = list(combinations(chicken, M))
# 집 위치 구하기
location = house()

result = find_shortest(location)
print(result)
