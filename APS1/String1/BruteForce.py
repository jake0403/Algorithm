p = 'is'    # 찾을 패턴
t = "This is a book~!"  #전체 텍스트

M = len(p)  #찾을 패턴의 길이
N = len(t)  #전체 텍스트의 길이

def BruteForce(p,t):
    i = 0   # t의 인덱스
    j = 0   # p의 인덱스

    while j < M and i < N:
        if t[i] != p[j]:
            i = i- j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M
    else: return -1

def BruteForce2(p,t):
    N = len(t)
    M = len(p)

    #시작 위치 컨트롤
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M:
            return i
    return -1
print(BruteForce2(p,t))
print(BruteForce(p,t))