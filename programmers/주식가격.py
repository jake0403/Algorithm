# from collections import deque
# def solution(prices):
#     n = len(prices)
#     prices = deque(prices)
#     answer = [0]*n
#     idx = []
#     while prices:
#         stock = prices.popleft()
#         cnt = 0
#         for p in prices:
#             if stock > p:
#                 cnt = 1
#                 break
#             else:
#                 cnt+=1
#         idx.append(cnt)
#
#     return idx



def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, n in enumerate(prices):
        while stack and n < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last

        stack.append(i)
    while stack:
        last = stack.pop()
        answer[last] = len(prices) - last - 1
    return answer

prices = [1,2,3,2,1]
print(solution(prices))