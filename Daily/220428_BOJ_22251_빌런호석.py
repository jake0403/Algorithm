import sys
input = lambda : sys.stdin.readline().strip()
# N : 최대 층수,  K : 층 자릿 수(10 =>2, 1000=>4)  P : 반전시킬 수 있는 횟수,  X : 현재 층 수
N, K, P, X = map(int, input().split())
answer = 0
# 디스플레이에서 나타내는 숫자들의 불 켜진 위치
num_arr = [[0,1,2,4,5,6], [2,6], [1,2,3,4,5], [1,2,3,5,6], [0,2,3,6], [0,1,3,5,6], [0,1,3,4,5,6], [1,2,6], [0,1,2,3,4,5,6], [0,1,2,3,5,6]]
num_info = [[0]*7 for _ in range(10)]
for i in range(10):
    for j in num_arr[i]:
        num_info[i][j] = 1
# 두 수의 차이를 비교한 값을 담을 10*10 행렬
diff = [[0]*10 for _ in range(10)]
# 차이 값을 반환하는 함수
def find_diff(x,y):
    cnt = 0
    for i in range(7):
        if num_info[x][i] != num_info[y][i]:
            cnt+=1
    return cnt
# dp 와 같이 해당 차이 나는 값을 10*10 행렬에 넣어둠
for i in range(10):
    for j in range(10):
        diff[i][j] = find_diff(i, j)
# 최대 N층 까지 비교
for i in range(1,N+1):
    if i == X:
        continue
    diff_cnt = 0
    x_, i_ = X, i
    # 자릿 수까지 반복하며 계산
    for j in range(K):
        diff_cnt += diff[x_%10][i_%10]
        x_ //= 10
        i_ //= 10
    if diff_cnt <= P :
        answer+=1
print(answer)