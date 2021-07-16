# 우선순위 큐 문제
# 큰 값이나 작은 값 또는 중앙 값을 효과적으로 찾기 위해서는 우선 순위 큐를 사용
# 중앙 값일 때는 왼쪽 큐, 오른쪽 큐를 나눠서 처리
# 그 전에는 DP를 활용해서 풀려고 했으나 시간초과
import heapq
import sys
input = sys.stdin.readline

N = int(input())
# num_array = [int(input()) for _ in range(N)]
# print(num_array[0])
# dp = [num_array[0]]
# for i in range(1,N):
#     dp.append(num_array[i])
#     x = i
#     while dp[x] < dp[x-1] and x != 0:
#         dp[x], dp[x-1] = dp[x-1], dp[x]
#         x-=1
#     print(dp[i//2])

# 왼쪽은 maxHeap(작은 값이 들어가야함) => heapq.heappop(left_h[1])을 하게 되면 큰 값부터 나옴
# 오른쪽은 minHeap(큰 값이 들어가야 함)
left_h, right_h  = [], []
for i in range(N):
    n = int(input())
    # 값이 같을 때는 (짝수 일 때) 왼쪽 큐에 넣음
    if len(left_h) == len(right_h):
        heapq.heappush(left_h, (-n, n))
    else:
        heapq.heappush(right_h, (n, n))

    # 왼쪽 큐에 오른쪽 큐보다 큰 값이 있을 수 있으므로 처리
    # 그럴려면 오른쪽 큐에 값이 있어야 함
    if right_h and left_h[0][1] > right_h[0][1]:
        left = heapq.heappop(left_h)[1]
        right = heapq.heappop(right_h)[1]
        heapq.heappush(left_h, (-right, right))
        heapq.heappush(right_h, (left, left))

    print(left_h[0][1])

