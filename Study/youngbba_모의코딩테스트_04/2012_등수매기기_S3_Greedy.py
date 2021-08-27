import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
num_arr = []
for i in range(N):
    num_arr.append(int(input()))
num_arr.sort()
ans = 0
for i in range(N):
    if i+1 != num_arr[i]:
        ans+= abs(i+1-num_arr[i])
print(ans)