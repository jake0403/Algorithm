# i : 방문지 번호
# n :
def f(i, n, k, s):
    global minV
    if i == k:  # 순열의 크기와 비교
        if p[0] == 1:
            arr.append(p[:k])
        #print(p[:k])
    else:
        for j in range(i, n):  # p[i]를 p[j]와 교환해 p[i]를 결정
            p[i], p[j] = p[j], p[i]
            f(i+1, n, k)  # p[i+1]을 결정하러 이동
            p[i], p[j] = p[j], p[i]  # 원래위치로 되돌리고 다음 j와 교환 준비


T = int(input())
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1
    minV = 10000
    print(f'#{tc} {minE}')