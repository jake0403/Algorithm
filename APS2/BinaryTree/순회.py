'''
5 4
2 1 2 4 4 3 4 5
'''
def preOrder(n):
    if n > 0:
        print(n, end=' ')
        preOrder(left[n])
        preOrder(right[n])

V , E = map(int, input().split())
edge = list(map(int, input().split()))

left = [0]*(V+1)
right = [0] * (V + 1)

pa = [0] * (V + 1)

for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]

    if left[n1] == 0:
        left[n1] = n2
    else:
        right[n1] = n2

    pa[n2] = n1

root = 0
for i in range(1, V+1):
    if pa[i] == 0:
        root = i
        break

preOrder(root)