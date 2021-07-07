n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
total = 0
for i,j in zip(a,b):
    total+=(i*j)

print(total)