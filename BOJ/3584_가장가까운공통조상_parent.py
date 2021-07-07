import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    V = int(input())
    parent = [0]*(V+1)
    for i in range(V-1):
        p, c = map(int, input().split())
        parent[c] = p
    cn1, cn2 = map(int, input().split())

    ans1, ans2 = [cn1], [cn2]

    while parent[cn1]:
        ans1.append(parent[cn1])
        cn1 = parent[cn1]

    while parent[cn2]:
        ans2.append(parent[cn2])
        cn2 = parent[cn2]

    for a in ans1:
        if a in ans2:
            answer = a
            break
    print(answer)