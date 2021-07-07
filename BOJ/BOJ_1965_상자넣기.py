n = int(input())
arr = list(map(int, input().split()))
# 상자 안들어가도 1 이므로 1로 초기화
dp = [1]*n
# 첫 번째 값은 크던 작던 무조건 1이므로 두 번째 상자부터 loop
for i in range(1,n):
    # 자신의 앞 상자들과 비교하며 크기 작을수록 비교
    for j in range(i):
        if arr[i] > arr[j]:
            # 자신보다 작은 상자가 넣은 값중 가장 많이 들어가 있는 상자 값 +1을 넣기
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
# stack = []
# stack.append(arr.popleft())
# i = 0
# while arr:
#     if arr[0] - stack[-1] > 0:
#         stack.append(arr.popleft())
#     else:
#         stack.pop()
#     i+=1
# print(len(stack))
