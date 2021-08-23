import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
body_arr = [list(map(int, input().split())) for _ in range(N)]

for i in body_arr:
    rank = 1
    for j in body_arr:
        if i[0] < j [0] and i[1] < j[1]:
            rank+=1
    print(rank, end= " ")