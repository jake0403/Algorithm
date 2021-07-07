# N = int(input())
# num_list = [[0]*N for x in range(N)]
# count = 0
# for i in range(N):
#     for j in range(N):
#         count += 1
#         num_list[i][j + (N-1-2*j)*(i%2)] = count
# print(num_list)
N = int(input())
cnt = 0
while N >=0:
    if N % 5 == 0:
        cnt+=(N//5)
        print(cnt)
        break
    N-=3
    cnt+=1
else:
    print(-1)