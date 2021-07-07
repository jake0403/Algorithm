def check2(ans):
    maxZ = 0
    if not ans:
        z_cnt = 0
        for i in range(N):
            for j in range(N):
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr = i + dr
                    nc = j + dc
                    if 0<=nr<N and 0<=nc<N and not arr[nr][nc]:
                        z_cnt+=1
                if maxZ < z_cnt:
                    maxZ = z_cnt
                    ans = [i,j]
    else:
        for a in ans:
            z_cnt = 0
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr = a[0] + dr
                nc = a[1] + dc
                if 0<=nr<N and 0<=nc<N and not arr[nr][nc]:
                    z_cnt+=1
            if maxZ < z_cnt:
                # if ans:
                #
                maxZ = z_cnt
                ans = [a[0],a[1]]
    return ans

def check1(student, arr):
    s_num = student[0]
    student = student[1:]
    maxF = 0
    ans = []
    for i in range(N):
        for j in range(N):
            # 친구 수 세기
            friend_cnt = 0
            if arr[i][j] == 0:
                # 상하좌우 체크
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nr = i + dr
                    nc = j + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in student:
                            friend_cnt+=1
                # 친구 수 많은 자리에 앉히기
                # 친구 수가 동일한 자리가 여러개라면 주변에 비어있는자리
                if maxF <= friend_cnt:
                    if maxF == friend_cnt:
                        ans.append([i,j])
                    else:
                        if ans:
                            arr[ans[0][0]][ans[0][1]] = 0
                        ans = [[i,j]]
                    maxF = friend_cnt
    # 주변에 좋아하는 학생이 앉지 않거나
    # 좋아하는 학생의 수가 같은 자리가 여러개라면
    if not ans or len(ans) > 1:
        ans = check2(ans)
        arr[ans[0]][ans[1]] = s_num
    if len(ans) == 1:
        arr[ans[0][0]][ans[0][1]] = s_num
    return





N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
arr = [[0]*(N) for _ in range(N)]
score = 0
score_table = {0:0, 1:1, 2:10, 3:100, 4:1000}
for s in students:
    check1(s, arr)


for s in students:
    for r in range(N):
        for c in range(N):
            cnt = 0
            if arr[r][c] == s[0]:
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in s[1:]:
                            cnt+=1
                score += score_table[cnt]

print(score)