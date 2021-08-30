import heapq

def solution(jobs):
    jobs.sort()
    N = len(jobs)
    pq = []
    # 첫 작업시간, 작업이 끝나는 시간(-1인 이유는 아직 pq에 값이 없기 때문)
    time, end = jobs[0][0], -1
    cnt = 0
    ans = 0

    while cnt < N:
        for s, t in jobs:
            if end < s <= time:
                heapq.heappush(pq,(t,s))
        if len(pq) > 0:
            end = time
            term, start = heapq.heappop(pq)
            cnt+=1
            time +=term
            ans += (time - start)
        else:
            time+=1
    return ans // N


def solution2(jobs):
    jobs.sort()
    ans = 0
    pq = []
    N = len(jobs)
    cnt, answer, now ,start = 0, 0, 0, -1

    while cnt < N:
        for s, j in jobs:
            if start < s <= now:
                heapq.heappush(pq, (j,s))
        if heapq:
            start = now
            j, s = heapq.heappop(pq)
            now += j
            ans += (now - s)
            cnt+=1
        else:
            now+=1
    return ans // N



jobs = [[0, 3], [1, 9], [2, 6]]

print(solution2(jobs))