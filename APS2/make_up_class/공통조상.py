# 부모 찾는 함수
def findRoot(n, arr):
    # 부모 인덱스를 기준으로 저장된 ch1, ch2에서
    # index 값을 활용해 거꾸로 부모를 찾음
    if n > 0:
        # ch1, ch2에 있는 노드의 인덱스는 부모를 뜻함
        if n in ch1:
            d = ch1.index(n)
            arr.append(d)
            findRoot(d,arr)
        elif n in ch2:
            d = ch2.index(n)
            arr.append(ch2.index(n))
            findRoot(d, arr)
        else:
            return
    return arr

def preOrder(n):
    global cnt
    if n > 0 :
        cnt+=1
        preOrder(ch1[n])
        preOrder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    # node 수, 간선 수, 공통 부모 갖는 자식 노드 2개
    V, E, Cn1, Cn2 = map(int, input().split())
    graph = list(map(int, input().split()))
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(0, E*2, 2):
        if not ch1[graph[i]]:
            ch1[graph[i]] = graph[i+1]
        else:
            ch2[graph[i]] = graph[i+1]
    # 부모의 노드가 순서대로 리스트에 저장됨
    a = findRoot(Cn1,[])
    b = findRoot(Cn2,[])

    if len(a) < len(b):
        a, b = b, a
    # 두 노드의 공통된 부모를 순회하면서 찾음
    # 먼저 나온 값은 가장 근접한 공통된 부모
    for i in range(len(a)):
        if b[i] in a:
            root = b[i]
            break
    cnt = 0
    # 공통된 부모의 전체 자식 수를 구함
    preOrder(root)
    print(f'#{tc} {root} {cnt}')