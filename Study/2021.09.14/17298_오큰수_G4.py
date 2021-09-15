import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))
result = [-1]*N
s = [0]
for i in range(1,N):
    while s and arr[s[-1]] < arr[i]:
        result[s.pop()] = arr[i]
    s.append(i)
print(*result)
# ans = []
# for i in range(N-1):
#     for j in range(i,N):
#         if arr[i] < arr[j]:
#             ans.append(arr[j])
#             break
#     if len(ans) != i+1:
#         ans.append(-1)
# ans.append(-1)

