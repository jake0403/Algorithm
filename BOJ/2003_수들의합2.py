N, M = map(int, input().split())
num_list = list(map(int, input().split()))
cnt  = 0
idx = 0
check = 0
while idx < N:
    for i in range(idx,N):
        check += num_list[i]
        if check == M:
            cnt+=1
            check = 0
            break
        elif check > M:
            check = 0
            break
    check = 0
    idx+=1
print(cnt)
