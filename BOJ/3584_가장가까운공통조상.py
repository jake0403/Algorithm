def findRoot(n, lst):
    if ch[n]:
        for i in range(1,V+1):
            if n in ch[i]:
                lst.append(i)
                findRoot(i, lst)
    return lst


import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    V = int(input())
    E = V -1
    ch= [[] for _ in range(V+1)]
    for i in range(E):
        p, c = map(int, input().split())
        ch[p]+=[c]
    cN1, cN2 = map(int, input().split())
    for i in range(len(ch)):
        if cN1 in ch[i]:
            ans1 = findRoot(i,[cN1,i])
        elif cN2 in ch[i]:
            ans2 = findRoot(i,[cN2,i])
    print(ans1, ans2)
    for a in ans1:
        if a in ans2:
            ans = a
            break
    print(ans)


'''
[[], [14, 13], [], [], [6, 10], [9], [15, 7], [], [5, 4, 1], [], [16, 11, 2], [], [], [], [], [], [3, 12]]
'''