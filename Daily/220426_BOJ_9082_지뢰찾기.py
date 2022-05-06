import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    N = int(input())
    arr_i = [int(x) for x in list(input())]
    arr_v = list(input())
    mine = 0
    for i in range(N):
        if i == 0:
            if arr_i[i] > 0 and arr_i[i+1] > 0:
                arr_i[i]-=1
                arr_i[i+1]-=1
                mine+=1
        elif i == N-1:
            if arr_i[i-1] > 0 and arr_i[i] > 0:
                arr_i[i-1] -=1
                arr_i[i] -=1
                mine+=1

        else:
            if arr_i[i-1] > 0 and arr_i[i] > 0 and arr_i[i+1] > 0:
                arr_i[i-1]-=1
                arr_i[i] -= 1
                arr_i[i+1]-=1
                mine+=1
    print(mine)