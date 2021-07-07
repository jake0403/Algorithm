from collections import deque
def rotation(lst, c):
    global ans
    lst = deque(lst)
    for i in range(c-1):
        lst.append(lst.popleft())
    return lst

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    K = K-1
    pw = input()
    C = N//4
    cnt  = 0
    ans = []
    while cnt < C:
        cnt+=1
        for i in range(0, N, C):
            ans.append(pw[i:i+C])
        pw = ''.join(rotation(pw, C))
    ans = list(set(ans))
    ans.sort(reverse=True)
    ans = [int(x,16) for x in ans]
    print(f'#{tc} {ans[K]}')