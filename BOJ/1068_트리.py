N = int(input())
tree = list(map(int, input().split()))
rmN = int(input())

def remove(ch, n):
    ch[n] = -2
    for i in range(N):
        if n == ch[i]:
            remove(ch,i)

remove(tree,rmN)
cnt = 0
for i in range(N):
    if tree[i] != -2 and i not in tree:
        cnt+=1
print(cnt)