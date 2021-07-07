def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    idx = 0
    while idx < n:
        if citations[idx] <= idx:
            break
        idx+=1
    return idx

citations = [1,7,0,1,6,4]
print(solution(citations))