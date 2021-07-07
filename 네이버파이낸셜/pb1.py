P = [4,4,2,4]
S = [5,5,2,5]

def solution(P,S):
    P.sort(reverse = True)
    S.sort(reverse = True)
    cnt = 0
    person = 0
    i = 0
    while sum(P) != 0:
        if P[person] < S[i]:
            S[i] -= P[person]
            P[person] = 0
            person+=1
            if person == len(P) and sum(P) == 0:
                cnt+=1
        else:
            P[person] -= S[i]
            S[i] = 0
            cnt+=1
            i+=1
    return cnt

print(solution(P,S))
