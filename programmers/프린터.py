from collections import deque
def solution(priorities, location):
    prior = [[v, i] for i, v in enumerate(priorities)]
    prior = deque(prior)
    cnt = 0
    print(prior)
    while True:
        maxP = max(prior)[0]
        v, i = prior.popleft()
        if v == maxP:
            cnt += 1
            if i == location:
                return cnt
        else:

            prior.append([v, i])



priorities = [2,1,3,2]
location = 2
print(solution(priorities, location))