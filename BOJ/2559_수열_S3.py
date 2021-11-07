import sys
input = lambda : sys.stdin.readline().strip()


N, K = map(int, input().split())

temp = list(map(int, input().split()))

max_temp = sum(temp[:K])
ans = max_temp
for i in range(K,N):
    max_temp= max_temp + temp[i] - temp[i-K]
    ans = max(max_temp, ans)
print(ans)