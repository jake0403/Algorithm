N, k = map(int, input().split())
foods = list(map(int, input().split()))
foods = [[v,i] for i,v in enumerate(foods)]
s1 = foods[k-1:]
s2 = foods[:k-1]
order = s1 + s2
result = []
idx = -1
while order:
    idx+=1
    n = len(order)
    min_num = min(order)[0]
    if min_num == order[idx][0]:
        result.append(order.pop(idx)[1]+1)
        idx = -1
    if idx == n:
        idx = -1
print(*result)