T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    fuel = list(map(int, input().split()))
    for i in range(m-1):

        if fuel[i] -