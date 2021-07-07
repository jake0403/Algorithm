def find_set(n):
    while n != MST[n]:
        n = MST[n]
    # 최상단 대표 값 반환
    return n


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    edge = []
    for i in range(E):
        fn, en, w = map(int,input().split())
        edge.append([w,fn,en])
    # 가중치 오름차순 정렬
    edge.sort()
    # V의 개수
    N = V+1
    # 0번 Vertex 부터 V번까지(자기 자신을 대표로 가지는)
    MST = [x for x in range(N)]
    # cnt : 개수 확인
    cnt = 0
    # tw : 총 가중치의 합
    tw = 0

    for w, fn, en in edge:
        rf = find_set(fn)
        re = find_set(en)
        # 사이클이 아닌 값만 총 가중치에 더하게 (최소 w 부터 오름차순 정렬했으니)
        if rf != re:
            # 노드 수 더하고
            cnt+=1
            # 총 가중치 더함
            tw +=w
            # 대표 원소 바꾸기(순서 상관 X)
            MST[re] = rf
            if cnt == N:
                break
    print(f'#{tc} {tw}')