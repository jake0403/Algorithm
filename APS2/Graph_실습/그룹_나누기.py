'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''
def find_set(x):
    if x == group[x]:
        return x
    else:
        return find_set(group[x])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    m_list = list(map(int, input().split()))
    group = [i for i in range(N+1)]
    cnt = 0

    for i in range(0,len(m_list),2):
        p1 = find_set(m_list[i])
        p2 = find_set(m_list[i+1])
        if p1 != p2:
            cnt+=1
            group[p2] = p1
            if cnt == N:
                break
    group = group[1:]
    ans = 0
    # group의 index가 자기 자신과 같을 때는 최상위
    for i in range(len(group)):
        if i+1 == group[i]:
            ans+=1
    print(group)
    print(f'#{tc} {ans}')