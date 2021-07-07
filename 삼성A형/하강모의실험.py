from pprint import pprint
# 장애물 저항력 구하는 함수
def w(r,c):
    global cnt
    if r+1 < N and arr[r][c] == arr[r+1][c]:
        cnt+=1
        w(r+1,c)
    arr[r][c] = cnt

def drop(r,c, cnt):
    for i in range(1,N):
        # 하강할 수 있을 경우
        if arr[i][r] == 0:
            arr[c-cnt][r], arr[i][r] = arr[i][r], arr[c-cnt][r]*1.9
            if cnt >0 :
                arr[i-cnt][r] = arr[i][r]
            c = i
        # 장애물이 있을 경우
        else:
            # 하강하는 힘이 더 큰 경우
            if arr[c][r] > arr[i][r]:
                arr[c][r] = arr[c][r] + arr[i][r]
                s = i
                while s < N and arr[s][r]:
                    # 합쳐진 길이 = cnt
                    cnt+=1
                    arr[s][r] = arr[c][r]
                    s+=1
            else:
                return


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(1, N):
            if arr[j][i] == 1:
                cnt = 1
                w(j,i)
    for i in range(N):
        if arr[0][i] == 1:
            drop(i,0,0)

    pprint(arr)