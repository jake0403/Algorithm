import sys
input = lambda : sys.stdin.readline().strip()

arr = input().split('-')
ans = 0

for i in arr[0].split('+'):
    ans += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)
# pm = []
# num = []
# N = len(arr)
# for i in range(N):
#     if not arr[i].isdigit():
#         if pm:
#             n = int(arr[pm[-1]+1:i])
#         else:
#             n = int(arr[:i])
#         pm.append(i)
#         num.append(n)
#     if i == N-1:
#         n = int(arr[pm[-1]+1:])
#         num.append(n)
# for i in range(len(pm)):
#     pm[i] = arr[pm[i]]
# print(pm, num)
#
# min_num = 0
# flag = 0
# for i in range(len(pm)):
#     if i == 0:
#         if pm[i] == '-':
#             min_num+=num[i]
#         else:
#             min_num+= (num[i]+num[i+1])
#     else:
#         if pm[i] == '-':
#