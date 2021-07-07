N = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, 1]
r = N-1
c = 0
change = 0
num_list = [[0]*N for x in range(N)]
num_list[N-1][0] = 1
#전체 개수 만큼 반복해 num_list에 값 넣어줌
for i in range(2,N**2+1):
    # 다음 값 넣어줄 row index 변경
    r += dr[change]
    # 다음 값 넣어줄 col index 변경
    c += dc[change]
    # num_list에 변경된 index 값에 i 넣어줌
    num_list[r][c] = i
    # 옆으로는 한칸 씩만 가니깐
    if change % 2 ==1:
        # change 값 변경
        change+=1
        # change 값이 3이면
        if change >= 3:
            # 0으로 초기화
            change = 0
    # 다음에 넣을 값 미리 확인
    nr = r + dr[change]
    nc = c + dc[change]
    if 0 <= nr < N and 0 <= nc < N and not num_list[nr][nc]:
        continue
    if change < 3:
        change += 1
    else:
        change = 0
for i in num_list:
    print(*i)