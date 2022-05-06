import heapq


def solution(operations):
    answer = []
    pq_min = []
    pq_max = []
    for oper in operations:
        m, o = oper.split()
        o = int(o)
        if m == "I":
            heapq.heappush(pq_min, o)
            heapq.heappush(pq_max, [-o, o])

        elif m == "D":
            if not pq_min:
                continue
            else:
                if o > 0:
                    rm = heapq.heappop(pq_max)
                    pq_min.remove(rm[1])
                else:
                    rm = heapq.heappop(pq_min)
                    pq_max.remove([-rm, rm])
    if not pq_min:
        answer = [0, 0]
    else:
        answer.append(heapq.heappop(pq_max)[1])
        answer.append(heapq.heappop(pq_min))

    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))