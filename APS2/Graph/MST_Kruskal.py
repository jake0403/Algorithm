'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
def find_set(x):
    while x != p[x]:        # 대표원소가 아니면
        x = p[x]        # x가 가리키는 정점으로 이동
    return x

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append((w,u,v))    # 가중치를 맨 앞으로(정렬하기 쉽게)

    edge.sort()     # 가중치 기준 오름차순 정렬

    p = [i for i in range(V+1)]          # 대표 원소 초기화 (자기 자신을 대표로 하는 Make-Set(x))

    # N개의 정점이 있으면 사이클이 생기지 않도록 N-1개의 간선을 선택
    # MST에 포함된 간선의 가중치의 합 구하기
    N = V+1     # 0~V번 까지의 정점
    cnt = 0
    total = 0   # 가중치의 합

    for w, u, v in edge:        # N-1개의 간선 선택 루프
        repU = find_set(u)
        repV = find_set(v)
        if repU != repV:      # 사이클을 형성하지 않으면 선택
            cnt+=1
            total += w  # 가중치 누적 합
            p[repV] = repU        # v의 대표원소를 u의 대표원소로 바꿈
            if cnt == N-1:
                break
    print(total)