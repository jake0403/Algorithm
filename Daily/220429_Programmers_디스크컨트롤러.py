jobs = [[0, 3], [1, 9], [2, 6]]

import heapq
def solution(jobs):
    jobs.sort()
    q = []
    N = len(jobs)
    cnt, now, total = 0, 0, 0
    start = -1
    while cnt < N:
        for job, time in jobs:
            if start < job <= now:
                heapq.heappush(q,[time, job])
        if q:
            start = now
            time, job = heapq.heappop(q)
            now += time
            total += (now - job)
            cnt += 1
        else:
            now+=1
    return total//N
print(solution(jobs))


