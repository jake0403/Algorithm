from collections import Counter
V = int(input())
E = int(input())
group = [i for i in range(V+1)]
network = []

def find_set(x):
    while x != group[x]:
        x = group[x]
    return x

for i in range(E):
    c1, c2 = map(int, input().split())
    network += [c1,c2]
cnt = 0
for i in range(0, E, 2):
    if network[i] > network[i+1]:
        network[i], network[i+1] = network[i+1], network[i]
    c1 = find_set(network[i])
    c2 = find_set(network[i+1])
    if c1 != c2 :
        cnt+=1
        group[c2] = c1
        if cnt == V:
            break
group = Counter(group[1:])
print(group[1])
