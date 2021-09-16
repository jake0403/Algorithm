'''
투포인터 문제
'''
p = [103,101,103,103,101,102,100,100,101,104]

def solution(p):
    answer = 0
    p.sort()
    L = 0
    R = 1
    N = len(p)
    while R < N:
        if p[L] < p[R]:
            answer+=1
            L+=1
            R+=1
        elif p[L] == p[R]:
            R+=1
    return answer

print(solution(p))