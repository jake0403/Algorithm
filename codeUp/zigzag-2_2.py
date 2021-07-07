N = int(input())
num_list = [[0]*N for x in range(N)]

count = 1
for i in range(N):
    if i%2 == 0:
        for j in range(N-1, -1, -1):
            num_list[i][j] = count
            count+=1
    else:
        for j in range(N):
            num_list[i][j] = count
            count+=1

for n in num_list:
    print(*n)

