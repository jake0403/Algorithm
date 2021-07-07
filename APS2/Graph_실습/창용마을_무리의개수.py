'''
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''

def find_set(x):
    while x != group[x]:
        x = group[x]
    return x

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    group = [i for i in range(V+1)]
    member = []
    for i in range(E):
        n1, n2 = map(int, input().split())
        member+=[n1,n2]
    cnt = 0
    for i in range(0, len(member),2):
        n1 = find_set(member[i])
        n2 = find_set(member[i+1])
        if n1 != n2:
           cnt+=1
           group[n2] = n1
           if cnt == V:
               break
    group = group[1:]
    ans = 0
    for i in range(len(group)):
        if i+1 == group[i]:
            ans+=1
    print(f'#{tc} {ans}')
    print(group)