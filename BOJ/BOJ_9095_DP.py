# n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
#  n이 3보다 클 때 f(n) = f(n-1) + f(n-2) + f(n-3)의 점화식 이용
T = int(input())
num_list = []
for tc in range(T):
    # 출력할 숫자 n을 num_list에 입력 받기
    num_list.append(int(input()))
# n이 1, 2, 3 일때의 방법의 수 저장
dp = [1,2,4]

# 3부터 => n-1, n-2, n-3의 값이 num_list index 값 [0,1,2]
for i in range(3,max(num_list)):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

for n in num_list:
    print(dp[n-1])