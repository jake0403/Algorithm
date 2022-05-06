priorities = [2,1,3,2]
location = 2

from collections import deque
def solution(priorities, location):
    q = deque([])
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    cnt = 0
    while True:
        max_p = max(q)[0]
        p, i = q.popleft()
        if p == max_p:
            cnt+=1
            if i == location:
                return cnt
        else:
            q.append([p,i])

print(solution(priorities, location))