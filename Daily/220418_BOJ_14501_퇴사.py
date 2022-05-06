import sys
input = lambda : sys.stdin.readline().strip()


def dfs(date, pay):
    global max_p
    if date == N:
        max_p = max(pay, max_p)
        return
    dfs(date+1, pay)
    if date + arr_t[date] <= N:
        dfs(date+arr_t[date], pay+arr_p[date])



N = int(input())
arr_t = []
arr_p = []
max_p = -1
for i in range(N):
    T, P = map(int, input().split())
    arr_t.append(T)
    arr_p.append(P)

dfs(0,0)
print(max_p)

