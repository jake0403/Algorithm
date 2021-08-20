import sys
input = lambda : sys.stdin.readline().strip()

num_list = list(map(int, input().split()))
N = len(num_list)
for i in range(N):
    for j in range(1, N):
        if num_list[j-1] > num_list[j]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
            print(*num_list)