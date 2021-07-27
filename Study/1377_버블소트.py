import sys
input = sys.stdin.readline

N = int(input())
num_list = [(int(input()),i) for i in range(N)]
sort_list = sorted(num_list)
result = []
for i in range(N):
    result.append(sort_list[i][1] - num_list[i][1])
print(max(result)+1)
